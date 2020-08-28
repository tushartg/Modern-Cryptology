import random
import constants as cons
from function import val, expand, perminv, perm, xor, ip, ipinv

f = open("bin_io.txt", "r+")
l = f.readlines()
f.close()

def key_set():
	key = []
	for _ in range(8):
		s = set()
		for i in range(64):
			s.add(bin(i)[2:].zfill(6))
		key.append(s)
	return key

key_3 = key_set()
for i in range(0, len(l), 2):
	p1, c1 = l[i].split()
	p2, c2 = l[i+1].split()
	
	xr = perminv(xor(xor(c1[32:], c2[32:]), xor(p1[:32], p2[:32])))
	p, q = expand(c1[:32]), expand(c2[:32])

	for i in range(len(key_3)):
		not_pos = set()
		for key in key_3[i]:
			g, h = xor(p[6*i:6*i+6], key), xor(q[6*i:6*i+6], key)
			g = cons.s[i][int(g[0]+g[5], 2)][int(g[1:5], 2)]
			h = cons.s[i][int(h[0]+h[5], 2)][int(h[1:5], 2)]
			if bin(g^h)[2:].zfill(4) != xr[4*i:4*i+4]:
				not_pos.add(key)
		key_3[i] = key_3[i]-not_pos
# print(key_3)

def rev_round(s, key):
	r = expand(s[:32])
	n = ""
	for i in range(len(key)):
		for k in key[i]:
			h = xor(r[6*i:6*i+6], k)
			h = cons.s[i][int(h[0]+h[5], 2)][int(h[1:5], 2)]
			n += bin(h)[2:].zfill(4)
	return xor(s[32:], perm(n))+s[:32]

key_2 = key_set()
for s in l:
	p, c = s.split()
	c = rev_round(c, key_3)
	SE = expand(c[:32])
	SO = perminv(xor(p[32:], c[32:]))

	for i in range(len(key_2)):
		not_pos = set()
		for key in key_2[i]:
			h = xor(SE[6*i:6*i+6], key)
			h = cons.s[i][int(h[0]+h[5], 2)][int(h[1:5], 2)]
			if h != int(SO[4*i:4*i+4], 2):
				not_pos.add(key)
		key_2[i] = key_2[i]-not_pos
# print(key_2)

key_1 = key_set()
for s in l:
	p, c = s.split()
	c = rev_round(rev_round(c, key_3), key_2)
	SE = expand(c[:32])
	SO = perminv(xor(p[:32], c[32:]))

	for i in range(len(key_1)):
		not_pos = set()
		for key in key_1[i]:
			h = xor(SE[6*i:6*i+6], key)
			h = cons.s[i][int(h[0]+h[5], 2)][int(h[1:5], 2)]
			if h != int(SO[4*i:4*i+4], 2):
				not_pos.add(key)
		key_1[i] = key_1[i]-not_pos
# print(key_1)

f = open("keys.txt", "w+")
def print_key(keys):
	for i in range(len(keys)):
		for key in keys[i]:
			f.write(key)
		if i!=7:
			f.write(" ")
print_key(key_3)
f.write("\n")
print_key(key_2)
f.write("\n")
print_key(key_1)
f.close()