import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle, os

def seg_model(target_img, model_name):

    if any((item == model_name) for item in os.listdir()):
        raise Exception("Such file already exists!")

    def tellme(s):
        print(s)
        plt.title(s, fontsize=16)
        plt.draw()

    image = mpimg.imread(target_img)
    ax = plt.gca()
    ax.set_xticks(np.arange(0, 1280, 50));
    ax.set_yticks(np.arange(0, 800, 50));
    ax.set_xticklabels(np.arange(0, 1280, 50));
    ax.set_yticklabels(np.arange(0, 800, 50));
    plt.imshow(image)
    plt.setp(plt.gca(), autoscale_on=False)

    folder_name = target_img.split('/')[1].split('_')[0]
    crop_pts = [folder_name]
    num = 0
    while True:
        pts = []
        while len(pts) < 2:
            pts = np.asarray(plt.ginput(2, timeout=-1))
            tellme('ok')
        crop_pts.append(pts)
        
        # visualize the cropped area with a red rectangle
        p1, p2 = pts
        pts = np.append(pts, np.array([p1[0],p2[1]]))
        pts = np.append(pts, np.array([p2[0],p1[1]]))
        x = [pts[0],pts[4],pts[2],pts[6]]
        y = [pts[1],pts[5],pts[3],pts[7]]
        ph = plt.fill(x, y, 'r', alpha = 0.7)
        
        num += 1
        tellme("Keyboard click to end. \nMouse click on figure to proceed to crop next car.")
        if plt.waitforbuttonpress():
            break

    pickle.dump(crop_pts, open(model_name, 'wb'))
    print("You have selected {} points. That is {} images to crop.".format(num*2, num))
    print("The input coordinates are saved as {}.".format(model_name))