A=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]

def change_matrixA(i, j, v):
    A[i][j] = v

change_matrixA(2,2, 16)
print(A)

v=[0]*30
w=[0]*30
v[1] = 16
v[29] = 16
print(sum(v))

B=[[0]*10]*10
def change_matrixB(i, j, v):
    B[i][j] = v
change_matrixB(2,2, 16)
change_matrixB(3,3, 17)
print(B)
