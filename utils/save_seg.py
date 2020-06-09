#!/usr/bin/env python3
import cv2
import pickle, os
from utils.ck_directory import ckdir
from utils.batch_save import save

def save_seg(target_img, model_name):

    if any((item == model_name) for item in os.listdir()):
        pts = pickle.load(open(model_name, 'rb'))    
    else:
        print('No such model found in the directory.')

    if os.path.isfile(target_img):
        dt, date = ckdir(target_img)
        img = cv2.imread(target_img)
        save(dt, date, img, pts)
    elif os.path.isdir(target_img):
        for file in os.listdir(target_img):
            path = os.path.join(target_img, file)
            dt, date = ckdir(path)
            img = cv2.imread(path)
            save(dt, date, img, pts)