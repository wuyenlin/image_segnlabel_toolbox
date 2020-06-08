#!/usr/bin/env python3
import cv2
import pickle, os
from utils.ck_directory import ckdir

def save_seg(target_img, model_name):
    if any((item == model_name) for item in os.listdir()):
        pts = pickle.load(open(model_name, 'rb'))    
    else:
        print('No such model in the directory.')

    ckdir(pts) # check
    date = pts[0]
    dt = (target_img.split('/')[-1]).split('.jpg')[0] 
    img = cv2.imread(target_img)

    for i in range(1, len(pts)):
        x1 , y1 = int(pts[i][0][0]), int(pts[i][0][1])
        x2 , y2 = int(pts[i][1][0]), int(pts[i][1][1])
        crop_img = img[y1:y2, x1:x2]
        img_name = dt + f"{i:03}" + '.jpg'
        out_path = os.path.join('PATCHES', date, img_name)
        cv2.imwrite(out_path, crop_img)

    print("All segmented images are saved to the 'PATCHES/{}' directory.".format(date))


if __name__ == "__main__":
    # example
    save_seg('original/2020-06-05_17.00_no.jpg','trondheim_pklot')