f = open("input.txt", "r+")
s = f.read()
f.close()

d = {}
d['i'] = 'S'
# d['e'] = 'E'
# d['u'] = 'A'
# d['k'] = 'O'

f = open("try_to_read.txt", "w+")
for i in s:
	if(i in d):
		f.write(d[i])
	else:
		f.write(i)
f.close()