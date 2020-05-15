import matplotlib.pyplot as plt
import cv2
import numpy as np


def getColorBGR(img):
    b = img.T[0].flatten().mean()
    g = img.T[1].flatten().mean()
    r = img.T[2].flatten().mean()
    return [b, g, r]


def plots(bgr, frameRate):
    bgrdata = np.array(bgr)
    time = np.arange(len(bgrdata)) / frameRate
    b = bgrdata[:, 0]
    g = bgrdata[:, 1]
    r = bgrdata[:, 2]
    fig = plt.figure('fingerRGB')
    axr = fig.add_subplot(3, 1, 1)
    axg = fig.add_subplot(3, 1, 2)
    axb = fig.add_subplot(3, 1, 3)
    axr.plot(time, r, 'r')
    axg.plot(time, g, 'g')
    axb.plot(time, b, 'b')


if __name__ == "__main__":
    print('start')
    fname = 'finger.mp4'
    cap = cv2.VideoCapture(fname)
    bgr = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        bgr.append(getColorBGR(frame))
    plots(bgr, cap.get(cv2.CAP_PROP_FPS))
    # plt.show()
    plt.savefig(fname+'.png')
    cap.release()
    print('end')
