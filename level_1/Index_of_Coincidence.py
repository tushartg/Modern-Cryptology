f = open("level_1.txt", "r+")
st = f.read()
f.close()

#Function to find the Index of coincidence of a block
def find_IOC(st):
	ch = {}
	for k in st:
		try:
			ch[k] += 1
		except:
			ch[k] = 1
	l = len(st)
	s = 0
	for k in ch:
		s += ch[k]*(ch[k]-1)
	return s/(l*(l-1))

print(find_IOC(st))