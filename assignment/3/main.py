import math
import numpy as np

# print matrix
def mprint(matrix):
    n = len(matrix)

    for i in range(0,n):
        for j in range(0,n):
            print(float(round(matrix[i][j], 2)), end=' ')
        print()

def vprint(vector):
    n = len(vector)

    for i in range(n):
        print(float(round(vector[i], 2)), end=' ')
    print()

def lu(A):
    n = A.shape[0]
    U = np.zeros((n, n), dtype=np.double)
    L = np.eye(n, dtype=np.double)
    for k in range(n):
        U[k, k:] = A[k, k:] - L[k,:k] @ U[:k,k:]
        L[(k+1):,k] = (A[(k+1):,k] - L[(k+1):,:] @ U[:,k]) / U[k, k]
    return L, U

# Ly = b
def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    
    y[0] = b[0] / L[0, 0]
    
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]  
    return y

# Ux = y
def backward_substitution(U, y):
    n = U.shape[0]
    
    x = np.zeros_like(y, dtype=np.double)
    
    x[-1] = y[-1] / U[-1, -1]
    
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

if __name__ == "__main__":

    n, m = map(int, input().split())

    A = []

    #get matrix A
    for i in range(n):
        row = list(map(int, input().split()))

        A.append(row)

    A = np.array(A)

    # َAx = b
    b = []
    for i in range(m):
        col = list(map(int, input().split()))

        b.append(col)

    L, U = lu(A)

    print('\nA =')
    mprint(A)

    print('\nL =')
    mprint(L)

    print('\nU =')
    mprint(U)

    print()
    for i in range(m):
        y = forward_substitution(L, b[i])
        x = backward_substitution(U, y)

        vprint(x)
