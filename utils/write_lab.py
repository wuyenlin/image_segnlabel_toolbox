import os

def write_label(folder):

    file = open('PATCHES', 'a')

    for file in folder:
        img_path = os.path.join(folder, file) # check how to get filename
        img = cv2.imread(img_path)

        cv2.imshow('sample', img)
        cmd = cv2.waitKey() 
        if cmd == ord('1'):
            file.write("{} 1\n".format(path))
            print('1')
            continue
        elif cmd == ord('0'):
            file.write("{} 0\n".format(path))
            print('0')
            continue
        elif cmd == 32: # space
            file.write("{}  \n".format(path))
            print('Skipped.')
            continue
        elif cmd == 27: # ESC
            print("Stopped.")
            break
    

    file.close()
    print("Finished labelling all files in current folder.")
    print("Label .txt file has been saved. Goodbye!")