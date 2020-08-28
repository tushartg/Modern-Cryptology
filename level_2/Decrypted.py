f = open("input.txt", "r+")
s = f.read()
f.close()

f = open("output.txt", "r+")
t = f.read()
f.close()

p = t.split("\n")
p.pop()
print(p)
f = open("Decrypted.txt", "w+")
for st in p:
	idx=0
	for i in s:
		if(i.isalpha()):
			if(i.isupper()):
				f.write(st[idx].upper())
			else:
				f.write(st[idx])
			idx += 1
		else:
			f.write(i)
	f.write("\n")
f.close()