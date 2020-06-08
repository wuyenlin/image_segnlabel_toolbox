import os

def ckdir(target_img):
    dt = (target_img.split('/')[-1]).split('.jpg')[0] 
    date = dt.split('_')[0]

    try:
        os.mkdir('PATCHES')
        os.mkdir('LABELS')
        os.mkdir(os.path.join('PATCHES', date))
    except(FileExistsError):
        pass

    return dt, date