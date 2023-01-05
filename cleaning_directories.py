#!/usr/bin/env python

import os 
import re
import shutil

IMAGES_FOLDER = "./imgs"

for path in os.listdir(IMAGES_FOLDER):
    if path.startswith("2022"):
        continue

    if path.endswith(".jpg"):
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
