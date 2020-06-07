from utils.seg import seg_model 

print("This is an image-cropping tool developed by Yen-Lin Wu.")
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

# elif x == '2':
