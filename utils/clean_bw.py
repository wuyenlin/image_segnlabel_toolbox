#!/usr/bin/env python3
import cv2
import os

def clean_bw(target_folder):
    for file in os.listdir(target_folder):
        path = os.path.join(target_folder, file)
        img = cv2.imread(path)
        print(img.shape)
        if img.shape[-1] == 1:
        # if len(img.shape) == 2:
            print("The file {} is deleted since it has shape {}.".format(file, img.shape))
            os.remove(file)
