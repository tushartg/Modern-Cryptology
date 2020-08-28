import matplotlib.pyplot as plt
import numpy as np

f = open("level_3.txt", "r+")
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

#Assuming a key of length period is used. We extract all 
#the character which will be shifted by the same amount 
#Array ar stores the character at the same inverval period
def make_partition(st, period):
	ar = []
	for j in range(period):
		i = j
		temp = []
		while(i < len(st)):
			temp.append(st[i])
			i += period
		ar.append(temp)
	return ar

a = []
b = []
#Here key_len is the assumed length of the key corresponding 
#to which Index of coindicence is calculated for the characted 
#with same shift i.e. every key_len th character
print(find_IOC(st))
# for key_len in range(1,31):
# 	score = 0
# 	for p in make_partition(st, key_len):
# 		score += find_IOC(p)
# 	print("key length:", key_len, end=", ")
# 	print("Average Index of Coindicence:", score/key_len)
# 	a.append(score/key_len)
# 	b.append(key_len)
# # print(b)

# plt.plot(b, a)
# plt.show()
# plt.xlabel('Characters')
# plt.ylabel('Frequency')
# plt.title('Frequency Analysis of the Text to decipher')
# plt.show()
# plt.savefig('Frequency_Analysis')
