import matplotlib.pyplot as plt
import numpy as np

f = open("level_3.txt", "r+")
s = f.read()
f.close()

a = [0 for i in range(26)]
b = []

for i in range(26):
	b.append(chr(ord('a')+i))

for i in s:
	if(i.isalpha()):
		a[ord(i)-ord('a')] += 1/(len(s)-1)

x = np.arange(26)
c = [(a[i], b[i]) for i in range(26)]
c.sort(reverse = True)

for k in range(26):
	a[k], b[k] = c[k][0], c[k][1]

plt.bar(x, a)
plt.xticks(x, b)
plt.xlabel('Characters')
plt.ylabel('Frequency')
plt.title('Frequency Analysis of the Text to decipher')
# plt.show()
plt.savefig('Frequency_Analysis')
