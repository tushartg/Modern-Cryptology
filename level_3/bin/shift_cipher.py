import matplotlib.pyplot as plt
import numpy as np

f = open("input.txt", "r+")
st = f.read()
f.close()

def shift_char(c, shift):
	a = 'a'
	if(c.isupper()):
		a = 'A'
	return chr((ord(c)-ord(a)+shift)%26+ord(a))

f = open("shift_cipher.txt", "w+")
for shift in range(26):
	f.write(str(shift+1)+". ")
	for i in st:
		if(i.isalpha()):
			f.write(shift_char(i, shift))
		else:
			f.write(i)
	f.write("\n\n")
f.close()