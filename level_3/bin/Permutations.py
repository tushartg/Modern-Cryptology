from itertools import permutations

def isvowel(a):
	vwl = 0
	for i in a:
		if(i in "aeiou"):
			vwl += 1
	return vwl

def change(a, shift):
	s = ""
	for i in a:
		s += chr((ord(i)-ord('a')+shift)%26+ord('a'))
	return s

f = open("level_3.txt", "r+")
s = f.read()
f.close()

a = s[:7]
for shift in range(0,26):
	b = change(a, shift)
	if(isvowel(b)<2):
		continue

	t = chr(ord('a')+shift)
	f = open("./per_and_shift/"+t+".txt", "w+")
	f.write("Shift: "+str(shift)+"\n")

	for per in permutations([0,1,2,3,4,5,6]):
		for i in per:
			f.write(b[i])
		for i in per:
			f.write(" "+str(i))
		f.write("\n")
	f.close()
	