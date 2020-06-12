import os
import cv2


def write_label(seg_img_folder):
    date = seg_img_folder.split('/')[-1]
    txt_path = 'LABELS/{}.txt'.format(date)
    txt_file_r = open(txt_path, 'r')
    labeled = [line.split()[0] for line in txt_file_r.readlines()]
    txt_file_r.close()
    files_to_label = [file for file in os.listdir(seg_img_folder) if file not in labeled]
    print(f"{len(labeled)} labeled. {len(files_to_label)} to go.")
    print("Keys: 1: car, 0: no car, ESC: quit, ANY OTHER KEY: skip")

    txt_file_a = open(txt_path, 'a')
    for file in files_to_label:
        img_path = os.path.join(seg_img_folder, file)
        img = cv2.imread(img_path)
        cv2.imshow('sample', img)
        cmd = cv2.waitKey()
        if cmd == ord('1'):
            txt_file_a.write("{} 1\n".format(img_path))
            print('1')
            continue
        elif cmd == ord('0'):
            txt_file_a.write("{} 0\n".format(img_path))
            print('0')
            continue
        elif cmd == 27:  # ESC
            print('Stopped.')
            break
        else:  # any other key
            txt_file_a.write("{} x\n".format(img_path))
            print('Skipped.')
            continue

    txt_file_a.close()
    print("Finished labelling all files in current folder.")
    print("The txt file has been saved in LABELS/. Goodbye!")
