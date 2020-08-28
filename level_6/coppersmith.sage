# Convert English Text message to their corresponding binary representation by replacing every character by their 8-bit ASCII representation.
def convert_text_to_binary(text):
    res = ""
    for c in text:
        res += bin(ord(c)).replace("0b", "").zfill(8)
    return res

# Convert binary message to their corresponding English text representation by taking 8-bits and replacing them with corresponding ASCII character.
def convert_binary_to_text(binary, length=8):
    if len(binary)%8 != 0:
        binary = binary.zfill(len(binary) + 8 - len(binary) % 8)
    res = ""
    for i in range(0, len(binary), length):
        res += chr(int(binary[i : i + 8], 2))
    return res

# find roots of a polynomial equation
def find_roots(f, modulus, beta, m, t, X):

    degree = f.degree()
    n = degree * m + t
    polynomial_ring = f.change_ring(ZZ)
    x = polynomial_ring.parent().gen()
    g = []
    for i in range(m):
        for j in range(degree):
            g.append((x * X)**j * modulus**(m - i) * polynomial_ring(x * X)**i)
    for i in range(t):
        g.append((x * X)**i * polynomial_ring(x * X)**m)


    lattice = Matrix(ZZ, n)

    for i in range(n):
        for j in range(i+1):
            lattice[i, j] = g[i][j]

    lattice = lattice.LLL()

    transformed_pol = 0
    for i in range(n):
        transformed_pol += x**i * lattice[0, i] / X**i

    small_roots = transformed_pol.roots()

    roots = []
    for root in small_roots:
        if root[0].is_integer():
            result = polynomial_ring(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

# Copper Smith Attack with know prefix as paddingText and assume lenth of suffix in range [0, maxLenMessage]
def copperSmithAttack(N, e, C, paddingText, maxLenOfMessage):
    Prefix = int(convert_text_to_binary(paddingText), 2)
    for _len in range(0, maxLenOfMessage+1, 4):
        P.<x> = PolynomialRing(Zmod(N))
        f = ((Prefix<<_len) + x)^e - C
        degree = f.degree()
        beta = 1
        epsilon = beta / 7
        m = ceil(beta**2 / (degree * epsilon))
        t = floor(degree * m * ((1/beta) - 1))
        X = ceil(N**((beta**2/degree) - epsilon))

        roots = find_roots(f, N, beta, m, t, X)
        
        if roots:
            return roots[0]

    print('No solution found\n')

# Implementation of RSA to encrypt and deprypt message from known public and private keys
class RSA:
    def __init__(self,n,exp):
        self.n = n
        self.exp = exp

    def power(self,m,e):
        if e==1:
            return mod(m , self.n)
        else:
            temp = mod(self.power(m,e//2) , (self.n))
            if e%2==0:
                return mod((temp*temp) , (self.n))
            else:
                temp =  mod((temp*temp) , (self.n))
                return mod((temp * mod(m ,(self.n))) , (self.n))

    def encryption(self,m):
        return self.power(m,self.exp)

    def decryption(self,c,d):
        return self.power(c,d)

e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 58851190819355714547275899558441715663746139847246075619270745338657007055698378740637742775361768899700888858087050662614318305443064448898026503556757610342938490741361643696285051867260278567896991927351964557374977619644763633229896668511752432222528159214013173319855645351619393871433455550581741643299
txt = "This door has RSA encryption with exponent 5 and the password is"

suffix = copperSmithAttack(N, e, C, txt, 300)
suffix = bin(suffix).replace("0b","")

txt_msg = txt+convert_binary_to_text(suffix)
print(txt_msg)

M = int(convert_text_to_binary(txt_msg), 2)

rsa = RSA(N,e)
c = rsa.encryption(M)
print(c == C)