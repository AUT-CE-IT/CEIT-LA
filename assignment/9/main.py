import matplotlib.pyplot as plt
import numpy as np

'''
in this function we use SVD to reduce the image size
but its quality reduced too

'''


def reduce(file_name, k):
    img = plt.imread(file_name)
    # first we convert to three array R G B (RED,GREEN,BLUE)
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    # apply SVD to these array
    UR, SR, VR = np.linalg.svd(R)
    UG, SG, VG = np.linalg.svd(G)
    UB, SB, VB = np.linalg.svd(B)
    # make three zero array two use just orthogonal values from zero to K
    SR_new = np.zeros((UR.shape[0], VR.shape[1]), dtype=int)
    SG_new = np.zeros((UG.shape[0], VG.shape[1]), dtype=int)
    SB_new = np.zeros((UB.shape[0], VB.shape[1]), dtype=int)
    # make new array from zero to K of orthogonal values of S matrix for RED
    for m in range(SR_new.shape[0]):
        for s in range(SR_new.shape[1]):
            if m == s and m <= k:
                SR_new[m][s] = SR[m]
    # make new array from zero to K of orthogonal values of S matrix for GREEN
    for m in range(SG_new.shape[0]):
        for s in range(SG_new.shape[1]):
            if m == s and m <= k:
                SG_new[m][s] = SG[m]
    # make new array from zero to K of orthogonal values of S matrix for BLUE
    for m in range(SB_new.shape[0]):
        for s in range(SB_new.shape[1]):
            if m == s and m <= k:
                SB_new[m][s] = SB[m]
    # use inner dot to make R G B from new matrices
    new_R = UR.dot(SR_new).dot(VR)
    new_G = UG.dot(SG_new).dot(VG)
    new_B = UB.dot(SB_new).dot(VB)
    # convert float value to int for R G B
    for s in range(new_R.shape[0]):
        for k in range(new_R.shape[1]):
            new_R[s][k] = int(new_R[s][k])

    for s in range(new_G.shape[0]):
        for k in range(new_G.shape[1]):
            new_G[s][k] = int(new_G[s][k])

    for s in range(new_B.shape[0]):
        for k in range(new_B.shape[1]):
            new_B[s][k] = int(new_B[s][k])

    # make new image from R G B And shows it with matplotlib
    new_img = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=int)
    new_img[:, :, 0], new_img[:, :, 1], new_img[:, :, 2], = new_R, new_G, new_B
    plt.imshow(new_img)
    plt.show()


if __name__ == '__main__':
    # do same thing for reduce image size for all K values and all images
    for i in range(1, 4):
        file = str(i) + ".bmp"
        reduce(file, 50)
        reduce(file, 10)
        reduce(file, 150)
        reduce(file, 250)
