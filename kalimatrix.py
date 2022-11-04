#operating matrix with numpy
import numpy as np

#input number matrix
X = np.array([[1, 3, 5], [5, 7, 9], [9, 11, 13]])
y = np.array([[2, 4, 6], [6, 8, 10], [10, 12, 14]])

print ("The multiplication of matrix X and y is : \n", np.multiply(X,y))

#input matrix with range of matrix
matriksA = np.matrix(range(9)) 
#build matrix 3*3
matriksA = np.reshape(matriksA,(3,3))

#input matrix with random number
matriksB = np.random.randint(1,20,(3,3))

print ("The multiplication of matrix A and B is : \n", np.multiply(matriksA,matriksB))

#operating matrix with for
matriksK = [
    [8, 18, 28],
    [9, 19, 29],
    [10, 20, 30]
]

matriksJ = [
    [4, 14, 24],
    [5, 15, 25],
    [6, 16, 26]
]

print("The multiplication of matrix K and J is : ")
for x in range(0, len(matriksK)):
    row = []
    for y in range(0, len(matriksK[0])):
        result = np.empty((3,3))
        for z in range(0, len(matriksK)):
            result += (matriksK[x][z] * matriksJ[z][y])
        print(result[x][y], end =' ')
    print("")
