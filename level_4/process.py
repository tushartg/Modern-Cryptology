import constants as cons
from function import val, ip

f = open("random_io.txt", "r+")
l = f.readlines()
f.close()

f = open("bin_io.txt", "w+")
for idx in range(len(l)):
	if idx:
		f.write("\n")
	a, b = l[idx].split()
	s = ip(val(b))
	f.write(ip(val(a))+" "+s[32:]+s[:32])
f.close()