f = open("random_output.txt", "r+")
l = f.readlines()
f.close()

d = {}
for s in l:
	s = s.strip()
	for i in s:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
print(sorted(d))