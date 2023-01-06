#!/usr/bin/env python

# import hashlib
import os 
# import re
# import shutil


IMAGES_FOLDER = "./imgs"
GIFS_FOLDER = "./gifs"

def create_gif(year, month, day):
    source_imgs = os.path.join(IMAGES_FOLDER, f"{year}/{month}/{day}")
    result_dir = os.path.join(GIFS_FOLDER, f"{year}/{month}")
    os.makedirs(result_dir, exist_ok=True)

    result_gif = os.path.join(result_dir, f"{year}-{month}-{day}.gif")

    command = f"ffmpeg -f image2 -framerate 18 -pattern_type glob -i '{source_imgs}/*.jpg' -loop -1 -vf scale=480:-1 '{result_gif}'"
    print(command)
    os.system(command)


def check_gif_existence(year, month, day):
    result_dir = os.path.join(GIFS_FOLDER, f"{year}/{month}")
    result_gif = os.path.join(result_dir, f"{year}-{month}-{day}.gif")

    return os.path.exists(result_gif)

# Iterate for every day-directory, checking if the counterpart GIF does exist
years = [directory for directory in os.listdir(IMAGES_FOLDER) if os.path.isdir(os.path.join(IMAGES_FOLDER, directory))]

for year in years:
    year_path = os.path.join(IMAGES_FOLDER, year)
    months = [month for month in os.listdir(year_path) if os.path.isdir(os.path.join(year_path, month))]

    for month in months:
        month_path = os.path.join(year_path, month)
        days = [day for day in os.listdir(month_path) if os.path.isdir(os.path.join(month_path, day))]
        
        for day in days:
            if not check_gif_existence(year, month, day):
                create_gif(year, month, day)
