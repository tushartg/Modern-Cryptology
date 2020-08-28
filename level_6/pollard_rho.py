import math
import random

def f(x):
	return (x**2+a)%n

n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
a = random.randint(1, n-1)
x = random.randint(1, n-2)+1
y = f(x)
p = math.gcd(abs(y-x), n)
while p == 1:
	a = random.randint(1, n-1)
	x = f(x)
	y = f(f(y))
	p = math.gcd(abs(y-x), n)
print(p)