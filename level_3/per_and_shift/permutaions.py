# from itertools import permutations 

# f = open("input.txt", "r")
# st = f.read()
# f.close()

# st = st.replace(".","")
# st = st.replace("!","")
# st = st.replace(":","")
# st = st.replace(",","")
# temp = st.replace(" ","")

# pms=list(permutations([0,1,2,3,4]))   #trying for block length 5
# #print(pms)
# def per_text(text, per):
# 	ans = ""
# 	for k in range(0, len(text), 5):
# 		a = list(text[k:k+5])
# 		b = [a[i] for i in per]
# 		for s in b:
# 			ans += str(s)
# 	return ans

# def make_indented(source, ref):
# 	ans = ""
# 	i, j = 0, 0
# 	while(j < len(ref)):
# 		if(ref[j]==" "):
# 			ans += " "
# 		else:
# 			ans += source[i]
# 			i+=1
# 		j+=1
# 	return ans

# def count_rep(text):
# 	arr = text.split()
# 	count = 0
# 	dic = {}
# 	for k in arr:
# 		if(len(k) == 3):
# 			try:
# 				dic[k] += 1
# 			except:
# 				dic[k] = 1
# 	for l in dic:
# 		if(dic[l] > 1):
# 			count += dic[l]
# 	return count		

# ar = []
# for k in pms:
# 	ar.append((count_rep(make_indented(per_text(temp, k), st)), k))
# ar = sorted(ar, reverse = True)

# t = per_text(temp, ar[0][1])

# f = open("input.txt", "r+")
# s = f.read()
# f.close()

# f = open("output.txt", "w+")

# idx=0
# for i in s:
# 	if(i.isalpha()):
# 		if(i.isupper()):
# 			f.write(t[idx].upper())
# 		else:
# 			f.write(t[idx])
# 		idx += 1
# 	else:
# 		f.write(i)
# f.write("\n")
# f.close()

from itertools import permutations 

f = open("input.txt", "r")
st = f.read()
f.close()

st = st.replace(".","")
st = st.replace("!","")
st = st.replace(":","")
st = st.replace(",","")
st = st.replace("_","")
temp = st.replace(" ","")

pms=[]
for s in [1,2,4,5,7,8,10,14]:
	pms += list(permutations(range(s)))   #trying for block length s

def per_text(text, per):
	size = len(per)
	ans = ""
	for k in range(0, len(text), size):
		a = list(text[k:k+size])
		b = [a[i] for i in per]
		for s in b:
			ans += str(s)
	return ans

def make_indented(source, ref):
	ans = ""
	i, j = 0, 0
	while(j < len(ref)):
		if(ref[j]==" "):
			ans += " "
		else:
			ans += source[i]
			i += 1
		j += 1
	return ans

def count_rep(text):
	arr = text.split()
	count = 0
	dic = {}
	for k in arr:
		try:
			dic[k] += 1
		except:
			dic[k] = 1
	for l in dic:
		if(dic[l] > 1):
			count += dic[l]
	return count		

ar = []
for k in pms:
	ar.append((count_rep(make_indented(per_text(temp, k), st)), k))

ar = sorted(ar, reverse = True)
# print(ar[0],ar[1])
# print(make_indented(per_text(temp, ar[0][1]), st))

t = per_text(temp, ar[0][1])

f = open("input.txt", "r+")
s = f.read()
f.close()

f = open("output.txt", "w+")

idx=0
for i in s:
	if(i.isalpha()):
		if(i.isupper()):
			f.write(t[idx].upper())
		else:
			f.write(t[idx])
		idx += 1
	else:
		f.write(i)
f.write("\n")
f.close()