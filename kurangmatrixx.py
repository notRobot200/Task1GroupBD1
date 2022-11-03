# A basic code for matrix input from user
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

print("Masukan element matriks1:")
matrix1 = [[int(input())for i in range (col)]for j in range(row)]
print ("matrix1:")
for i in range (row):
    for j in range (col):
        print(format(matrix1 [i][j], "<3") , end="")
    print()

print("Masukan element matriks2:")
matrix2 = [[int(input())for i in range (col)]for j in range(row)]
print ("matrix2:")
for i in range (row):
    for j in range (col):
        print(format(matrix1 [i][j], "<3") , end="")
    print()

result = [[0 for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        result [i][j] = matrix1 [i][j] - matrix2 [i][j]
for i in range(row):
    for j in range (col):
        print(result [i][j],end = "")
    print()