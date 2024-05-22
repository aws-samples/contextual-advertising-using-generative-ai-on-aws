import os
import boto3
import time
import cv2
import datetime
from pathlib import Path
import json
from urllib.request import urlretrieve
from termcolor import colored

def download_vtt(response):
    output_file = 'transcript.vtt'
    urlretrieve(
        response['TranscriptionJob']['Subtitles']['SubtitleFileUris'][0],
        output_file
    )
    return output_file

def transcribe(bucket, path, file, media_format="mp4", language_code="en-US", verbose=True):

    # start transcription job
    transcribe_response = start_transcription_job(
        bucket, 
        path,
        file, media_format, language_code)

    # wait for completion
    transcribe_response = wait_for_transcription_job(
        transcribe_response['TranscriptionJob']['TranscriptionJobName'], 
        verbose)

    return transcribe_response

def start_transcription_job(bucket, path, file, media_format="mp4", language_code="en-US"):

    # create a random job name
    job_name = '-'.join([
        Path(file).stem,
        os.urandom(4).hex(),
    ])

    key = path+'/'+file

    transcribe_client = boto3.client('transcribe')

    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode=language_code,
        MediaFormat=media_format,
        Media={
            'MediaFileUri': f"s3://{bucket}/{key}",
        },
        Subtitles={
            'Formats': [
                'vtt',
            ],
        },
    )

    return response

def wait_for_transcription_job(job_name, verbose=True):
    transcribe_client = boto3.client('transcribe')

    while True:
        try:
            response = transcribe_client.get_transcription_job(
                TranscriptionJobName=job_name
            )
            transcription_job_status = response['TranscriptionJob']['TranscriptionJobStatus']
            if verbose: 
                print(f"wait_for_transcription_job: status = {transcription_job_status}")
            if transcription_job_status in ['COMPLETED', 'FAILED']:
                return response
            time.sleep(4)
        except Exception as e:
            print(f"Error fetching transcription job status: {e}")
            raise

def estimate_transcribe_cost(video_file):
    transcribe_batch_per_min = 0.02400

    # create video capture object
    cap = cv2.VideoCapture(video_file)
    # count the number of frames
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    # calculate duration of the video
    duration = round(frames / fps)
    transcribe_cost = round(transcribe_batch_per_min * (duration / 60), 4)


    return {
        'cost_per_min': transcribe_batch_per_min,
        'duration': duration,
        'estimated_cost': transcribe_cost,
    }

def display_transcription_cost(mp4_file):
    transcribe_cost = estimate_transcribe_cost(mp4_file)

    print('\nEstimated cost to Transcribe video:', colored(f"${transcribe_cost['estimated_cost']}", 'green'), f"in us-east-1 region with duration: {transcribe_cost['duration']}s")
    
    return transcribe_cost


def download_transcript(response):
    output_file = 'transcript.json'
    urlretrieve(
        response['TranscriptionJob']['Transcript']['TranscriptFileUri'],
        output_file
    )
    return output_file




