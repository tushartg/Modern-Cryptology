import constants as cons

def val(s):
	n = ""
	for i in s:
		n += bin(ord(i)-ord('f'))[2:].zfill(4)
	return n

def expand(s):
	n = ""
	for i in cons.expand:
		n += s[i-1]
	return n

def perminv(s):
	n = ""
	for i in cons.perminv:
		n += s[i-1]
	return n

def perm(s):
	n = ""
	for i in cons.perm:
		n += s[i-1]
	return n

def xor(s, t):
	n = ""
	for i in range(len(s)): 
		if s[i] == t[i]:
			n += '0'
		else:
			n += '1'
	return n

def ip(s):
	n = ""
	for i in cons.ip:
		n += s[i-1]
	return n

def ipinv(s):
	n = ""
	for i in cons.ipinv:
		n += s[i-1]
	return n

def enc(s):
	n = ""
	for i in range(16):
		p = int(s[4*i:4*i+4], 2)
		n += chr(ord('f')+p)
	return n