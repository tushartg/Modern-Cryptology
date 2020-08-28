from pyfinite import ffield
from pyfinite import genericmatrix
F=ffield.FField(7)
import itertools
def multiply_F128(n, m):
	ans = 0
	for i in range(8):
		if n & (1<<i):
			ans = ans^(m<<i)

	for i in range(13, 6, -1):
		if ans&(1<<i):
			ans ^= 1<<i
			ans ^= 1<<(i-6)
			ans ^= 1<<(i-7)
	return ans

# F=ffield.FField(7)
def power (a,b):
	ans=F.Multiply(1,1)
	while(b>0):
		if (b&1) == 1:
			ans = F.Multiply(ans,a)
		a = F.Multiply(a,a)
		b=b>>1
	return ans

keys= [[0 for i in range(8)] for j in range(8)]
keys[0][0]= {(26, 48), (113, 43), (115, 125)}
keys[1][1]= {(23, 125), (48, 58), (56, 4)}
keys[2][2]= {(70, 67), (124, 28), (60, 80)}
keys[3][3]= {(125, 15), (40, 45), (89, 31)}
keys[4][4]= {(111, 22), (77, 119), (66, 115)}
keys[5][5]= {(74, 111), (44, 66), (9, 19)}
keys[6][6]= {(52, 37), (103, 126), (99, 12)}
keys[7][7]= {(84, 15), (72, 96), (98, 73)}
E=[None for i in range(8)]

def find_a21():
	inp=[]
	out=[]
	f=open('.//2//2.txt','r')
	st=f.readlines()
	f.close()
	for s in st:
		tinp=[]
		tout=[]
		temp=s.split()
		for i in range(8):
			tinp.append((ord(temp[0][2*i])-ord('f'))*16+(ord(temp[0][2*i+1])-ord('f')))
			tout.append((ord(temp[1][2*i])-ord('f'))*16+(ord(temp[1][2*i+1])-ord('f')))
		inp.append(tinp)
		out.append(tout)
	possibles=set()
	for m in range(128):
		tp=set()
		for i in keys[0][0]:
			for j in keys[1][1]:
				for a21 in range(128):
					an1_1=power(inp[m][0],i[0])
					an1_2=F.Add(F.Multiply(an1_1,a21),F.Multiply(power(inp[m][1],j[0]),j[1]))
					# print(power(F.Multiply(an1_1,i[1]),i[0]),a21)+F.Multiply(power(an1_2,j[0]))
					an2_2=F.Add(F.Multiply(power(F.Multiply(an1_1,i[1]),i[0]),a21),F.Multiply(power(an1_2,j[0]),j[1]))
					temp=power(an2_2,j[0])
					if temp==out[m][1]:
						tp.add((i[0],i[1],j[0],j[1],a21))
		#print(tp)	
		if m==0:
			possibles=tp
		else:
			possibles=possibles.intersection(tp)
	# print(possibles)		
	if len(possibles)==1:
		keys[0][0]=list(possibles)[0][1]
		keys[1][1]=list(possibles)[0][3]
		keys[1][0]=list(possibles)[0][4]
		E[0]=list(possibles)[0][0]
		E[1]=list(possibles)[0][2]
	# print(keys[0][0],keys[1][0],keys[1][1])	

def encrypt_till_this_row_incomplete_row(inp,i):
	# apply E
	output_1=[power(inp[j],E[j]) for j in range(i)]
	# apply A
	output_2=[None for p in range(i)]
	for p in range(i):
		sums=0
		for q in range(p,p+1):
			sums=F.Add(sums,F.Multiply(output_1[q],keys[p][q]))
		output_2[p]=sums
	#apply E	
	output_3=[power(output_2[j],E[j]) for j in range(i)]
	# output_4=[None for p in range(i)]
	# for p in range(i):
	# 	sums=0
	# 	for q in range(p+1):
	# 		sums=F.Add(sums,F.Multiply(output_3[q],keys[p][q]))
	# 	output_4[p]=sums
	# #apply A	
	# output_5=[power(output_4[j],E[j]) for j in range(i)]
	# print(output_1,output_3,output_5)
	return [output_1,output_3]

def divi(a,b):
	for i in range(128):
		if F.Multiply(i,b)==a:
			return i	
	
def encrypt_till_this_row_complete_row(inp,i):
	# apply E
	output_1=[power(inp[j],E[j]) for j in range(i+1)]
	# apply A
	output_2=[None for p in range(i)]
	for p in range(i):
		sums=0
		for q in range(p+1):
			sums=F.Add(sums,F.Multiply(output_1[q],keys[p][q]))
		output_2[p]=sums
	#apply E	
	output_3=[power(output_2[j],E[j]) for j in range(i)]
	# output_4=[None for p in range(i)]
	# for p in range(i):
	# 	sums=0
	# 	for q in range(p+1):
	# 		sums=F.Add(sums,F.Multiply(output_3[q],keys[p][q]))
	# 	output_4[p]=sums
	# #apply A	
	# output_5=[power(output_4[j],E[j]) for j in range(i)]
	# print(output_1,output_3,output_5)
	return [output_1,output_3]
			
def find_rest_elements(p,q):
	inp=[]
	out=[]
	f=open('.//'+str(p+1)+'//'+str(p-q+1)+'.txt','r')
	st=f.readlines()
	f.close()
	for s in st:
		tinp=[]
		tout=[]
		temp=s.split()
		for i in range(8):
			tinp.append((ord(temp[0][2*i])-ord('f'))*16+(ord(temp[0][2*i+1])-ord('f')))
			tout.append((ord(temp[1][2*i])-ord('f'))*16+(ord(temp[1][2*i+1])-ord('f')))
		inp.append(tinp)
		out.append(tout)
	# print(inp)
	# print(out)		
	possibles=set()		
	for m in range(128):
		interm_inp=encrypt_till_this_row_complete_row(inp[m],p)	
		tp=set()
		for var in range(128):
			sum=0
			for i in range(p,q,-1):
				sum=F.Add(sum,F.Multiply(interm_inp[0][i],keys[p][i]))
			ans_1=F.Add(sum,F.Multiply(var,interm_inp[0][q]))
			sum=0
			for i in range(p-1,q,-1):
				sum=F.Add(sum,F.Multiply(interm_inp[1][i],keys[p][i]))
			an1_2=F.Add(F.Add(sum,F.Multiply(var,interm_inp[1][q])),F.Multiply(power(ans_1,E[p]),keys[p][p]))
			temp=power(an1_2,E[p])
			if temp==out[m][p]:
				tp.add(var)
		# print(tp)			
		if m==0:
			possibles=tp
		else:
			possibles=possibles.intersection(tp)
	print(p,q,possibles)		
	if len(possibles)==1:
		keys[p][q]=list(possibles)[0]

def find_next_diagonal_elements(p):
	inp=[]
	out=[]
	f=open('.//'+str(p+1)+'//2'+'.txt','r')
	st=f.readlines()
	f.close()
	for s in st:
		tinp=[]
		tout=[]
		temp=s.split()
		for i in range(8):
			tinp.append((ord(temp[0][2*i])-ord('f'))*16+(ord(temp[0][2*i+1])-ord('f')))
			tout.append((ord(temp[1][2*i])-ord('f'))*16+(ord(temp[1][2*i+1])-ord('f')))
		inp.append(tinp)
		out.append(tout)
	# print(inp)
	# print(out)		
	possibles=set()		
	for m in range(128):
		interm_inp=encrypt_till_this_row_incomplete_row(inp[m],p)		
		tp=set()
		for i in keys[p][p]:
			for var in range(128):
				an1_2=F.Add(F.Multiply(interm_inp[0][p-1],var),F.Multiply(power(inp[m][p],i[0]),i[1]))
				an2_2=F.Add(F.Multiply(interm_inp[1][p-1],var),F.Multiply(power(an1_2,i[0]),i[1]))
				temp=power(an2_2,i[0])
				if temp==out[m][p]:
					tp.add((i[0],i[1],var))
		# print(tp)			
		if m==0:
			possibles=tp
		else:
			possibles=possibles.intersection(tp)
	print(p,p-1,possibles)		
	if len(possibles)==1:
		keys[p][p]=list(possibles)[0][1]
		keys[p][p-1]=list(possibles)[0][2]
		E[p]=list(possibles)[0][0]

def find_main_diagonal_elements():
	inp=[]
	out=[]		
	for i in range(8):
		tinp=[]
		tout=[]	
		f=open('.//'+str(i+1)+'//'+'1.txt','r')
		st=f.readlines()
		f.close()	
		for s in st:
			temp=s.split()
			tinp.append((ord(temp[0][2*i])-ord('f'))*16+(ord(temp[0][2*i+1])-ord('f')))
			tout.append((ord(temp[1][2*i])-ord('f'))*16+(ord(temp[1][2*i+1])-ord('f')))
		inp.append(tinp)
		out.append(tout)	
	for p in range(8):
		possibles=set()
		for m in range(128):
			temp=set()		
			for a in range(0,128):
				for E in range(1,127):
					tep=power(F.Multiply(a,power(F.Multiply(a,power(inp[p][m],E)),E)),E)
					if tep==out[p][m]:
						temp.add((E,a))					
			if m==0:
				possibles=temp
			else:				
				possibles=possibles.intersection(temp)
		keys[p][p]=possibles
		print(p,p,keys[p][p])
	for p in range(8):
		E.append(list([k[0] for k in keys[p][p]]))	
	return

# find_main_diagonal_elements(inp,out)	
find_a21()
for i in range(2,8):
	find_next_diagonal_elements(i)
for i in range(2,8):
	for j in range(i-2,-1,-1):
		find_rest_elements(i,j)	
for k in keys:
	for l in k:
		print(l,end=" ")
	print()
# print(E)

def inv_E(output):
	ans=[None for i in range(8)]
	for i in range(8):
		for j in range(128):
			if power(j,E[i])==output[i]:
				ans[i]=j
				break
	return ans
def inv_A(output,keys_inv):
	ans=[None for i in range(8)]
	for i in range(8):
		sum=0
		for j in range(8):
			sum=F.Add(F.Multiply(keys_inv[i,j],output[j]),sum)
		ans[i]=sum	
	return ans
# def inv_A1(output,keys_inv):
# 	ans=[None for i in range(8)]
# 	for i in range(8):
# 		sum=0
# 		for j in range(8):
# 			sum=F.Add(F.Multiply(keys_inv[i][j],output[j]),sum)
# 		ans[i]=sum	
# 	return ans	

def encode(inp):
	output=[]
	for i in range(16):
		output.append((ord(inp[2*i])-ord('f'))*16+(ord(inp[2*i+1])-ord('f')))
	# print(output)		
	output[0:8]=[power(output[i],E[i]) for i in range(8)]
	output[0:8]=inv_A1(output[0:8],keys)
	output[0:8]=[power(output[i],E[i]) for i in range(8)]
	# output[0:8]=inv_A(output[0:8],keys)
	# output[0:8]=[power(output[i],E[i]) for i in range(8)]
	output[8:16]=[power(output[i],E[i-8]) for i in range(8,16)]
	output[8:16]=inv_A1(output[8:16],keys)
	output[8:16]=[power(output[i],E[i-8]) for i in range(8,16)]
	# output[8:16]=inv_A(output[8:16],keys)
	# output[8:16]=[power(output[i],E[i-8]) for i in range(8,16)]
	return output	

def decode(out):
	Add= lambda x,y : F.Add(x,y)
	Mul = lambda x,y: F.Multiply(x,y)
	Sub = lambda x,y: F.Subtract(x,y)
	Div = lambda x,y: divi(x,y) 	
	m = genericmatrix.GenericMatrix(size=(8,8),zeroElement=0,identityElement=1,add=Add,mul=Mul,sub=Sub,div=Div)
	for i in range(8):
		m.SetRow(i,keys[i])	
	output=[]
	for i in range(16):
		output.append((ord(out[2*i])-ord('f'))*16+(ord(out[2*i+1])-ord('f')))
	print(output)		
	# keys_inv=[[keys[i][j] for j in range(8)] for i in range(8)]
	# det=1
	# for i in range(8):
	# 		det=F.Multiply(det,keys[i][i])
	# print(det)		
	# for i in range(8):
	# 	for j in range(8):
	# 		keys_inv[i][j]=div(keys[i][j],det)
	keys_inv=m.Inverse()
	print(keys_inv)	
	output[0:8]=inv_E(output[0:8])
	output[0:8]=inv_A(output[0:8],keys_inv)
	output[0:8]=inv_E(output[0:8])
	output[0:8]=inv_A(output[0:8],keys_inv)
	output[0:8]=inv_E(output[0:8])
	output[8:16]=inv_E(output[8:16])
	output[8:16]=inv_A(output[8:16],keys_inv)
	output[8:16]=inv_E(output[8:16])
	output[8:16]=inv_A(output[8:16],keys_inv)
	output[8:16]=inv_E(output[8:16])	
	return output

def to_char(arr):
	st=""
	for i in range(16):
		pre=arr[i]//16
		post=arr[i]%16
		st+=chr(pre+ord('f'))
		st+=chr(post+ord('f'))
	return st	

def dec(s):
	n = ""
	for i in s:
		n += bin(ord(i)-ord('f'))[2:].zfill(4)
	return chr(int(n, 2))

s = to_char(decode("gkftmrfrfolimtgrlrihgniummflhkio"))
print(s)
for i in range(len(s)>>1):
	print(dec(s[2*i:2*i+2]), end = '')
print()

# print(to_char(encode("gkftmrfrfolimtgrlrihgniummflhkio")))
# a="gkftmrfrfolimtgrlrihgniummflhkio"
# print(F.Multiply(34,104))
