import faiss
import numpy as np
from functools import cmp_to_key
from numpy import dot
from numpy.linalg import norm


def create_index(dimension):
    index = faiss.IndexFlatIP(dimension) # cosine similarity
    return index

def index_frames(index, frame_embeddings):
    for item in frame_embeddings:
        embedding = np.array([item['embedding']])
        index.add(embedding)
    return index

def cosine_similarity(a, b):
    cos_sim = dot(a, b) / (norm(a) * norm(b))
    return cos_sim

# ascending sort by the starting shot_id first and then descending sort by the ending shot_id
def cmp_min_max(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    return b[1] - a[1]

def search_similarity(index, frame, k = 20, min_similarity = 0.80, time_range = 30):
    idx = int(frame['frame_no'])

    embedding = np.array([frame['embedding']])

    D, I = index.search(embedding, k)

    similar_frames = [
        {
            'idx': int(i),
            'similarity': float(d)
        } for i, d in zip(I[0], D[0])
    ]

    # filter out lower similiarity
    similar_frames = list(
        filter(
            lambda x: x['similarity'] > min_similarity,
            similar_frames
        )
    )

    similar_frames = sorted(similar_frames, key=lambda x: x['idx'])

    # filter out frames that are far apart from the current frame idx
    filtered_by_time_range = [{
        'idx': idx,
        'similarity': 1.0
    }]
    # filtered_by_time_range = [similar_frames[0]]

    for i in range(0, len(similar_frames)):
        prev = filtered_by_time_range[-1]
        cur = similar_frames[i]

        if abs(prev['idx'] - cur['idx']) < time_range:
               filtered_by_time_range.append(cur)

    return filtered_by_time_range



