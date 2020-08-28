import math

def babylonian(n):
	x = n
	y = 1
	while(x > y):
	    x = (x+y)>>1
	    y = n//x
	return x

N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
e = 5

q = []
a = e
b = N

while b != 0:
	q.append(int(a/b))
	r = a % b
	a = b
	b = r

n = len(q)
k = [[0 for j in range(n)] for i in range(n)]
d = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
	k[i][i] = q[i]
	d[i][i] = 1

for j in range(n):
	for i in range(j - 1, -1, -1):
		k[i][j] = q[i] * k[i + 1][j] + d[i + 1][j]
		d[i][j] = k[i + 1][j]

for i in range(n):
	if k[0][i] !=0 and (e * d[0][i] - 1) % k[0][i] == 0:
		phi = int( (e * d[0][i] - 1) / k[0][i] )
		M = N - phi + 1
		if M * M < 4 * N:
			continue
		p = ( M - babylonian(M * M - 4 * N)  )>>1
		if p * p - M * p + N == 0:
			print( p, int( N / p ) )
			break