#!/usr/bin/env python3
from utils.seg import seg_model 
from utils.save_seg import save_seg
from utils.write_lab import write_label

def main():
    print("===============================================================")
    print("==This is an image-segmentation tool developed by Yen-Lin Wu.==")
    print("===============================================================")

    print("The order of operation is listed as follows:")
    print("1: When you have a new image to segment and you want to CREATE a segmentation MASK.")
    print("2: When you have a segmentation mask to use and you want to SAVE segmented images using that mask.")
    print("3: When you have segmented images and want to LABEL them.\n")
    print("Please note : a) this toolbox only accepts files in jpg format.")
    print("              b) the jpg files should be named in the format of 'YYYY-MM-DD_hh.mm.jpg'.\n")
    x = input("Please choose a desired action:")

    if x == '1':
        print("Mode 1. Create new segementation mask.")
        model_name = input("Decide the NAME your mask will be saved as : (e.g. mymask) \n") 
        target_img = input("Give path to the image to be segmented : (e.g. path/to/image.jpg) \n")
        print('The model will be saved as {}.'.format(model_name))
        seg_model(target_img, model_name)

    elif x == '2':
        print("Mode 2. Now you'll be saving small segmented images.")
        target_img = input("Give path to TARGET IMAGE : (e.g. path/to/image.jpg) \n")
        model_name = input("Input mask name : (e.g. mymask) \n")
        save_seg(target_img, model_name)
    
    elif x == '3':
        print("Mode 3. Now you'll be manually LABELLING for the segmented images.")
        seg_img_folder = input("Give path to Segmented image FOLDER : (e.g. PATCHES/2020-06-08) \n")
        print("Please start labelling.")
        write_label(seg_img_folder)

if __name__ == "__main__":
    main()