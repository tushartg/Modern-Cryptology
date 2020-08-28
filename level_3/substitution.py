f = open("substitution.txt", "r+")
s = f.read()
f.close()

f = open("decrypted.txt", "w+")
d = {}
d['e'] = 'E'
d['t'] = 'A'
d['u'] = 'T'
d['b'] = 'H'
d['c'] = 'O'
d['k'] = 'I'
d['i'] = 'S'
d['o'] = 'N'
d['h'] = 'L'
d['m'] = 'U'
d['g'] = 'W'
d['w'] = 'Y'
d['y'] = 'R'
d['n'] = 'G'
d['v'] = 'D'
d['z'] = 'P'
d['s'] = 'V'
d['a'] = 'B'
d['p'] = 'K'
d['d'] = 'F'
d['r'] = 'C'
d['x'] = 'M'
d['l'] = 'Q'
d['q'] = 'j'
idx=0
for i in s:
	if i in d:
		f.write(d[i])
	else:
		f.write(i)
f.write("\n")
f.close()