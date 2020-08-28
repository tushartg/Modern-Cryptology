f = open("random_output.txt", "r+")
l = f.readlines()
f.close()

a = {}
o = {}
for s in l:
	s = s.strip()
	for i in range(len(s)):
		if i&1 == 0:
			if s[i] in o:
				o[s[i]] += 1
			else:
				o[s[i]] = 1
		if s[i] in a:
			a[s[i]] += 1
		else:
			a[s[i]] = 1
print("all charaters: ", sorted(a))
print("odd charaters: ", sorted(o))