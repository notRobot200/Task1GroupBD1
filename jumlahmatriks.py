# penjumlahan matrix 3x3

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[2,3,4],
	[6,5,4],
	[9,7,5]]


hasil = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# rumus baris
for i in range(len(X)):
# rumus kolom
	for j in range(len(X[0])):
		hasil[i][j] = X[i][j] + Y[i][j]

for r in hasil:
	print(r)