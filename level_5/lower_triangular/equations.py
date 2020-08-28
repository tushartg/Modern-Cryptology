import numpy
from function import dec 

for folder in range(1, 9):
	print("P is in the row: ", folder)
	s = [[] for i in range(8)]

	for idx in range(1<<8):
		f = open("./"+str(folder)+"/"+str(idx+1)+".txt", "r+")
		l = f.readlines()
		f.close()

		a = []
		for i in range(8):
			a.append([0 for i in range(1<<7)])
		for t in l:
			b, c = t.split()
			for i in range(len(c)>>1):
				a[i][dec(c[2*i:2*i+2])] ^= 1
		for i in range(8):
			s[i].append(a[i])

	for i in range(8):
		print("rank ", i+1, ": ", numpy.linalg.matrix_rank(numpy.matrix(s[i])))
	print()