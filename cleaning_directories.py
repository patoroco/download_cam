#!/usr/bin/env python

import hashlib
import os 
import re
import shutil


IMAGES_FOLDER = "./imgs"

for path in os.listdir(IMAGES_FOLDER):
    if not path.endswith(".jpg"):
        continue

    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    m = re.search(pattern, path)
    year = m.group(1)
    month = m.group(2)
    day = m.group(3)

    new_directory = os.path.join(IMAGES_FOLDER, f"{year}/{month}/{day}")
    os.makedirs(new_directory, exist_ok=True)
    old_path = os.path.join(IMAGES_FOLDER, path)
    new_path = os.path.join(new_directory, path)
    print(f"{old_path} --> {new_path}")

    shutil.move(old_path, new_path)

MERGING_PATHS = "./imgs/2023/01/05"
hashes = {}

for path in os.listdir(MERGING_PATHS):
    if not path.endswith(".jpg"):
        continue

    file_path = os.path.join(MERGING_PATHS, path)
    with open(file_path, "rb") as f:
        data = f.read()
        md5hash = hashlib.md5(data).hexdigest()

        if hashes.get(md5hash):
            print(f"{file_path} --> EXISTE!")

        hashes[md5hash] = file_path
        
        print(f"{file_path} --> {md5hash}")
