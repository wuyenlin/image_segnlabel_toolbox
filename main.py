from utils.seg import seg_model 
from utils.save_seg import save_seg
from utils.write_lab import write_label

def main():
    print("===========================================================")
    print("==This is an image-cropping tool developed by Yen-Lin Wu.==")
    print("===========================================================")
    print("0: When you have a new image to segment and you want to create a segmentation mask.")
    print("1: When you have a segmentation mask to use and you want to save segmented images using that mask.")
    print("2: When you have segmented images and want to label them.")
    x = input("Please choose the desired action:")

    if x == '0':
        print("Mode 0. Create new segementation mask/model for Trondheim Parking Lot model.")
        model_name = 'trondheim_pklot'
        path = 'original/2020-06-05_17.00_no.jpg'
        print('The model will be saved as {}.'.format(model_name))
        seg_model(path, model_name)

    elif x == '1':
        print("Mode1. Now you'll be making small segmented images.")
        target_img = input("Give path to TARGET IMAGE: ")
        model_name = input("Input model name: ")
        save_seg(target_img, model_name)
    
    elif x == '2':
        print("Mode 2. Now you'll be manually inputting labels for the segmented images.")
        sem_img_folder = input("Give path to Segmented image FOLDER: ")
        write_label(seg_img_folder)

if __name__ == "__main__":
    main()