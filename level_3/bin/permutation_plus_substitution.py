f = open("level_3.txt", "r+")
s = f.read()
f.close()

p = [0,1,3,2,4]
# t = ""
f = open("output.txt", "w+")
for i in range(0,len(s),5):
	a = s[i:i+5]
	for j in p:
		f.write(a[j])

		# t += a[j]
# print(t)
		# f.write(a[j])