import os
from shutil import rmtree
from PIL import Image, ImageDraw
from io import BytesIO
import base64
import json
    
def rmdir(directory):
    try:
        if os.path.isdir(directory):
            rmtree(directory)
    except Exception as e:
        print(e)

def mkdir(directory):
    try:
        if not os.path.isdir(directory):
            os.mkdir(directory)
    except Exception as e:
        print(e)

def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format='JPEG')
    return base64.b64encode(buff.getvalue()).decode('utf8')

def skip_frames(frames, max_frames = 80):
    if len(frames) < max_frames:
        return frames

    # miminum step = 2
    skip_step = max(round(len(frames) / max_frames), 2)

    output_frames = []
    for i in range(0, len(frames), skip_step):
        output_frames.append(frames[i])
    
    return output_frames

def create_grid_image(image_files, max_ncol = 10, border_width = 2):
    should_resize = len(image_files) > 50

    first_image = Image.open(image_files[0])
    width, height = first_image.size

    if should_resize:
        width = width // 2
        height = height // 2
        first_image = first_image.resize((width, height))

    ncol = max_ncol
    if len(image_files) < max_ncol:
        ncol = len(image_files)

    nrow = len(image_files) // ncol
    if len(image_files) % ncol > 0:
        nrow += 1
    
    # Create a new image to hold the grid
    grid_width = width * ncol
    grid_height = height * nrow
    grid_image = Image.new("RGB", (grid_width, grid_height))

    draw = ImageDraw.Draw(grid_image)
    # Paste the individual images into the grid
    for i, image_file in enumerate(image_files):
        image = Image.open(image_file)
        if should_resize:
            image = image.resize((width, height))
        x = (i % ncol) * width
        y = (i // ncol) * height
        grid_image.paste(image, (x, y))
        # draw border
        draw.rectangle((x, y, x + width, y + height), outline=(0, 0, 0), width=border_width)
    
    return grid_image

def create_composite_images(frames):
    reduced = skip_frames(frames, 280)
    # print(f"{len(frames)} -> {len(reduced)}")

    composite_images = []

    for i in range(0, len(reduced), 28):
        frames_per_image = reduced[i:i+28]
        composite_image = create_grid_image(frames_per_image, 4)
        composite_images.append(composite_image)

    return composite_images