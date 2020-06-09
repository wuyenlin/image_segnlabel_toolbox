import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle, os

def seg_model(target_img, model_name):

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
            # add if loop to check if it follows diagonal rule
            tellme('ok')
        crop_pts.append(pts)
        # ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=5)
        num += 1
        tellme("Keyboard click to end; mouse click on figure to proceed to crop next car.")
        if plt.waitforbuttonpress():
            break
        # for p in ph:
        #     p.remove()

    pickle.dump(crop_pts, open(model_name, 'wb'))
    print("You have selected {} points. That is {} images to crop.".format(num*2, num))
    print("The input coordinates are saved as {}.".format(model_name))

    # add condition to check if mask exists