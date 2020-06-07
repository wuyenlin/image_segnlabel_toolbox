import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle

def seg_model(path, model_name):

    def tellme(s):
        print(s)
        plt.title(s, fontsize=16)
        plt.draw()

    image = mpimg.imread(path)
    ax = plt.gca()
    ax.set_xticks(np.arange(0, 1280, 50));
    ax.set_yticks(np.arange(0, 800, 50));
    ax.set_xticklabels(np.arange(0, 1280, 50));
    ax.set_yticklabels(np.arange(0, 800, 50));
    plt.imshow(image)
    plt.setp(plt.gca(), autoscale_on=False)

    crop_pts = []
    while True:
        pts = []
        while len(pts) < 4:
            pts = np.asarray(plt.ginput(4, timeout=-1))
            tellme('ok')
        crop_pts.append(pts)
        ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=5)
        tellme("Keyboard click to end; mouse click on figure to proceed to crop next car.")
        if plt.waitforbuttonpress():
            break
        for p in ph:
            p.remove()

    with open(model_name, 'wb') as f:
        pickle.dump(crop_pts, f)
