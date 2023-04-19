from prime_generator import PRIMES_UNDER_1000
from prime_generator import check_small_primes
from prime_generator import generate_1024_prime,pow_mod
from re import sub

class RSA:
    def __init__(self):
        pair = generate_1024_prime()
        self.p = pair[0]
        self.q = pair[1]
        print(self.p,self.q)
        self.n = self.p*self.q
        self.phi = (self.p-1)*(self.q-1)
        self.e = 65537
        x,y = self.__xgcd(self.e,self.phi)
        if x<0:
            x = x+self.phi
        self.d = x

        

    def get_public_key(self):
        return self.n,self.e
    

    def get_private_key(self):
        return self.n, self.d
    

    def __xgcd(self,a,b):
        if b ==0:
            return 1,0
        else:
            x,y = self.__xgcd(b,a%b)
            x,y = y,(x-(a//b)*y)
            return x,y
        
    # def to_int(self,lst):
    #     n = 0
    #     for i, x in enumerate(reversed(lst)):
    #         n += x * 26^i
    #     return n
    
    # def to_text(self,)

    # def denumerify(self,nums: list):
    #     return "".join([chr((x % 26) + 65) for x in nums])

    # def decrypt(self,c: int, n: int, d: int):
    #     return self.deintegerify(pow_mod(c, d, n))
    
    # def deintegerify(self,n):
    #     rems = []
    #     while n > 0:
    #         rems.append(n % 26)
    #         n = n // 26
    #     return self.denumerify(reversed(rems))
    
    # def encode(self,text):
    #     stripped = sub(r"[^a-zA-Z]", "", text)
    #     return stripped.upper()

    
    # def numerify(self,text):
    #     return [(ord(x) - 65) for x in self.encode(text)]
    
    # def integerify(self,text):
    #     n = 0
    #     for i, x in enumerate(reversed(self.numerify(text))):
    #         n += x * 26^i
    #     return n

    def encrypt(self,msg:int):
        return pow_mod(msg,self.e,self.n)
    def decrypt(self,cipher:int):
        return pow_mod(cipher,d,self.n)
    

    

    