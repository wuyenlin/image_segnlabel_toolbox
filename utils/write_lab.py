import os
import cv2

def write_label(seg_img_folder):
    
    date = seg_img_folder.split('/')[-1]
    txt_path = 'LABELS/{}.txt'.format(date)
    txt_file = open(txt_path, 'a')

    for file in os.listdir(seg_img_folder):
        img_path = os.path.join(seg_img_folder, file)
        img = cv2.imread(img_path)
        cv2.imshow('sample', img)
        cmd = cv2.waitKey() 
        if cmd == ord('1'):
            txt_file.write("{} 1\n".format(img_path))
            print('1')
            continue
        elif cmd == ord('0'):
            txt_file.write("{} 0\n".format(img_path))
            print('0')
            continue
        elif cmd == 32: # space
            txt_file.write("{} x\n".format(img_path))
            print('Skipped.')
            continue
        elif cmd == 27: # ESC
            print('Stopped.')
            break

    txt_file.close()
    print("Finished labelling all files in current folder.")
    print("The txt file has been saved in LABELS/. Goodbye!")