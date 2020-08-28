import constants as cons
from function import val, expand, perm, xor, ip, ipinv

def rev_round(s, key):
	r = expand(s[:32])
	n = ""
	for i in range(len(key)):
		h = xor(r[6*i:6*i+6], key[i])
		h = cons.s[i][int(h[0]+h[5], 2)][int(h[1:5], 2)]
		n += bin(h)[2:].zfill(4)
	return xor(s[32:], perm(n))+s[:32]

def dec(p):
	p = ip(val(p))
	p = p[32:]+p[:32]
	f = open("keys.txt", "r+")
	for s in f.readlines():
		p = rev_round(p, s.split())
	p = ipinv(p)
	for i in range(8):
		print(int(p[8*i:8*i+8], 2), end='')

s = "mugulrhnrstmohmjhnlfmhusnrnfskgn"
for i in range(len(s)>>4):
	dec(s[16*i:16*i+16])
print()	