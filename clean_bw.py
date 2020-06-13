#!/usr/bin/env python3
import cv2
import os

def clean_bw(target_folder):
    for file in os.listdir(target_folder):
        path = os.path.join(target_folder, file)
        img = cv2.imread(path)
        if len(img.shape) == 2:
            print("The file {} is deleted since it has shape {}.".format(file, img.shape))
            os.remove(file)

if __name__ == "__main__":
    for weather in os.listdir('PATCHES'):
        path1 = os.path.join('PATCHES', weather)
        for date in os.listdir(path1):
            path2 = os.path.join(path1, date)
            for camera in os.listdir():
                path3 = os.path.join(path2, camera)
                try:
                    clean_bw(path3)
                except FileNotFoundError:
                    continue