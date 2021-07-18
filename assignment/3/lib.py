import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [5,6,2], [4,5,2], [2,4,8] ])
P, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

# for i in range(0,n):
#         maxElem = abs(U[i][i])
#         maxRow = i

#         for k in range(i+1, n):
#             if(abs(U[k][i] > maxElem)):
#                 maxElem = abs(U[k][i])
#                 maxRow = k

#         for k in range(i, n):
#             temp = U[maxRow][k]
#             U[maxRow][k] = U[i][k]
#             U[i][k] = temp

#         for k in range(i+1, n):
#             c = -U[k][i]/float(U[i][i])
#             L[k][i] = c
#             for j in range(i,n):
#                 U[k][j] += c*U[i][j]

#         for k in range(i+1, n):
#             U[k][i] = 0