import numpy as np

np.warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt


def a_mat(rows, lam):
    mat = np.vstack((np.eye(rows), np.sqrt(lam) * (np.roll(np.eye(rows - 1, rows), 1) + -np.eye(rows - 1, rows))))
    return mat


def b_vec(mat, rows):
    reshape = mat.reshape((rows, 1))
    b = np.vstack((reshape, np.zeros((rows - 1, 1))))

    return b


def normal(mat, v):
    # (AtA)-1 At b
    tmat = np.transpose(mat)
    invm = np.linalg.inv(np.matmul(tmat, mat))

    vmat = np.matmul(tmat, v)

    return np.matmul(invm, vmat)


def least_square(mat, lam):
    rows = len(mat)

    A = a_mat(rows, lam)
    v = b_vec(mat, rows)

    # sq = np.linalg.lstsq(A, v)[0]
    return normal(A, v)


def display(mat, lam):
    plt.plot(mat, label='noisy')
    plt.plot(least_square(mat, np.power(10, lam)), 'red',label='denoised')
    plt.title(r"$\lambda=%d$" % np.power(10, lam))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    mat = np.load('btc_price.npy')
    n = len(mat)

    plt.plot(mat)
    plt.show()

    for i in np.arange(1, 6, 1):
        display(mat, i)