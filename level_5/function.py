def dec(s):
	n = ""
	for i in s:
		n += bin(ord(i)-ord('f'))[2:].zfill(4)
	return int(n, 2)

def xor(s, t):
	n = ""
	for i in range(len(s)): 
		if s[i] == t[i]:
			n += '0'
		else:
			n += '1'
	return n

def enc(c):
	s = bin(c)[2:].zfill(8)
	n = ""
	for i in range(len(s)>>2):
		p = int(s[4*i:4*i+4], 2)
		n += chr(ord('f')+p)
	return n

def multiply_F128(n, m):
	print(bin(n)[2:].zfill(8), bin(m)[2:].zfill(8))
	ans = 0
	for i in range(8):
		if n & (1<<i):
			ans = ans^(m<<i)

	for i in range(13, 6, -1):
		if ans&(1<<i):
			ans ^= 1<<i
			ans ^= 1<<(i-6)
			ans ^= 1<<(i-7)
	return bin(ans)[2:].zfill(8)

s, t = "mkmlmgmhlololulnmllulkmolpllmpmh", ""
for i in range(len(s)>>1):
	print(chr(dec(s[2*i:2*i+2])), end = '')
