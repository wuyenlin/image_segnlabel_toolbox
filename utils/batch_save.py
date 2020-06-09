#!/usr/bin/env python3
import cv2
import pickle, os
from utils.ck_directory import ckdir

def save(dt, date, img, pts):

    for i in range(1, len(pts)):
        x1 , y1 = int(pts[i][0][0]), int(pts[i][0][1])
        x2 , y2 = int(pts[i][1][0]), int(pts[i][1][1])
        crop_img = img[y1:y2, x1:x2]

        img_name = dt + '_' + f"{i:03}" + '.jpg'
        out_path = os.path.join('PATCHES', date, img_name)
        is_written = cv2.imwrite(out_path.encode('unicode-escape').decode(), crop_img)
        print("Saved as {}.".format(out_path))
        if is_written:
            print("Saved {}/{}".format(i, len(pts)-1))
        else:
            raise Exception("Could not write image.")

    print("All segmented images are saved to \n'PATCHES/{}'.".format(date))