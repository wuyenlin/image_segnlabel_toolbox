#!/usr/bin/env python3
from ck_directory import ckdir
import cv2
import os, pickle

def ckdir(pts):
    date = pts[0]
    try:
        os.mkdir('PATCHES')
        os.mkdir('LABELS')
        os.mkdir(os.path.join('PATCHES', date))
    except(FileExistsError):
        pass

def save_seg(input_path, model_name, out_path):
    for item in os.listdir():
        if item == model_name:
            pts = pickle.load(open(model_name, 'rb'))    
        else:
            print('No such model in the directory.\n')

    ckdir(pts)
    img = cv2.imread(input_path)

    cv2.imshow('sample', img)
    cmd = cv2.waitKey() 