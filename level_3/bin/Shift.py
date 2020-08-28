f = open("level_3.txt", "r+")
st = f.read()
f.close()

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

def chi_sq(st):
	#dictionary dic stores the frequency of standard Englist text
	dic={}
	dic['a']=8.167
	dic['b']=1.492
	dic['c']=2.202
	dic['d']=4.253
	dic['e']=12.702
	dic['f']=2.228
	dic['g']=2.015
	dic['h']=6.094
	dic['i']=6.966
	dic['j']=0.153
	dic['k']=1.292
	dic['l']=4.025
	dic['m']=2.406
	dic['n']=6.749
	dic['o']=7.507
	dic['p']=1.929
	dic['q']=0.095
	dic['r']=5.987
	dic['s']=6.327
	dic['t']=9.356
	dic['u']=2.758
	dic['v']=0.978
	dic['w']=2.560
	dic['x']=0.150
	dic['y']=1.994
	dic['z']=0.077
	ch={}
	for k in st:
		try:
			ch[k]+=1
		except:
			ch[k]=1
	l=len(st)
	for p in dic:
		dic[p]=dic[p]*l/100			
	ans=0
	for m in ch:
		ans+=((ch[m]-dic[m])**2)/dic[m]
	return ans	

def product(ar_list):
    if not ar_list:
        yield ()
    else:
        for a in ar_list[0]:
            for prod in product(ar_list[1:]):
                yield (a,)+prod

def shift_char(c, shift):
	return chr((ord(c)-ord('a')+shift)%26+ord('a'))

#From calculation of Index_of_Coincidence we get the block length 
#to be 9 Now we calculate the key of length 9 
f_ans = []
tmp = make_partition(st, 20)

key = ""
for gh in tmp:
	ans = []	
	for shift in range(26):
		original_text = ""
		for p in gh:
			original_text += shift_char(p, shift)
		ans.append([chi_sq(original_text), original_text, shift])

	ans.sort()
	# print("Top 3 candidate for the keys %dth character:"%(len(key)+1), end = ' ')
	for i in range(3):
		print(shift_char('a', -ans[i][2]), end = ' ')
	print()

	if(ans[1][0]-ans[0][0]<2.5):
		f_ans.append([ans[0][2], ans[1][2], ans[2][2]])
	elif(ans[1][0]-ans[0][0]<5 or gh==tmp[-1]):
		f_ans.append([ans[0][2], ans[1][2]])
	else:		
		f_ans.append([ans[0][2]])
ciphers = list(product(f_ans))
# print(ciphers)
f = open("output.txt", "w+")
for arr in ciphers:
	a = ""
	for i in range(len(st)):
		a += shift_char(st[i], arr[i%9])
	f.write(a)
	f.write("\n")
f.close()