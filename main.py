from utils.seg import seg_model 
#from utils.save_seg import save_seg
#from utils.write_lab import write_label

def main():
    print("===========================================================")
    print("==This is an image-cropping tool developed by Yen-Lin Wu.==")
    print("===========================================================")
    x = input("Please choose the desired action:")

    if x == '0':
        print("Mode 0, create new segementation mask for Trondheim Parking Lot model.")
        model_name = 'trondheim_pklot'
        path = 'original/2020-06-05_17.00_no.jpg'
        seg_model(path, model_name)

    elif x == '1':
        path = input("Give path to TARGET IMAGE: ")
        name = input("Input model name: ")
        seg_model(path, name)


if __name__ == "__main__":
    main()