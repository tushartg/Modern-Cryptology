import math

def bpow(a, b):
	res = 1
	while b > 0:
		if b & 1:
			res *= a
			if res > n:
				res %= n
		a = a * a
		b >>= 1
	return res

f = open("rsa.txt", "w+")
# n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
r = 15
# n = 70348807
f.write("r : " + str(r) + "\n")
for a in range(2,3):
	num = a
	for b in range(2, r + 1):
		num = bpow(num, b)
	num = (num+n-1)%n
	f.write("a^r!-1 : " + str(num) + "\n")
	if num:
		f.write("gotcha\n")
		f.write(str(math.gcd(num, n))+"\n")
		break
f.write("Shut your brain off!")
f.close()