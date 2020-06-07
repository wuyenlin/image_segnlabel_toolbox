import os

def ckdir(pts):
    date = pts[0]
    try:
        os.mkdir('PATCHES')
        os.mkdir('LABELS')
        os.mkdir(os.path.join('PATCHES', date))
    except(FileExistsError):
        pass