import os
import cv2


def write_label(seg_img_folder):
    date = seg_img_folder.split('/')[-1]
    txt_path = 'LABELS/{}.txt'.format(date)
    try:
        with open(txt_path, 'r') as txt_file_r:
            labeled = [line.split()[0] for line in txt_file_r.readlines()]
    except FileNotFoundError:
        labeled = []
    img_files = [os.path.join(seg_img_folder, filename) for filename in os.listdir(seg_img_folder)]
    files_to_label = [file for file in img_files if file not in labeled]
    print(f"{len(labeled)} labeled. {len(files_to_label)} to go.")
    print("Keys: 1: car, 0: no car, ESC: quit, ANY OTHER KEY: skip")

    txt_file_a = open(txt_path, 'a')
    for file in files_to_label:
        img = cv2.imread(file)
        cv2.imshow('sample', img)
        cmd = cv2.waitKey()
        if cmd == ord('1'):
            txt_file_a.write("{} 1\n".format(file))
            print('1')
            continue
        elif cmd == ord('0'):
            txt_file_a.write("{} 0\n".format(file))
            print('0')
            continue
        elif cmd == 27:  # ESC
            print('Stopped.')
            break
        else:  # any other key
            txt_file_a.write("{} x\n".format(file))
            print('Skipped.')
            continue

    txt_file_a.close()
    print("Finished labelling all files in current folder.")
    print("The txt file has been saved in LABELS/. Goodbye!")
