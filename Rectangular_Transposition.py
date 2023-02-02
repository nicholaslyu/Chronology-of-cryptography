
from re import sub
import random
import string
class Rect:
    
    def __init__(self,key:str):
        if not key.isalpha():
            raise Exception("Key must only contain alphabet characters.")  
        if len(set(key)) != len(key):
            raise Exception("Key must avoid repeat characters.")
        if key.isupper() == False:  
            key = key.upper()
        self.key = key
        self.n = len(key)
        self.__key_order = [sorted(list(self.key)).index(x) for x in self.key]
        # self.__invert_key = [self.__key_order.index(i) for i in range(self.n)]

    def __encode(self,text: str):
        stripped = sub(r"[^a-zA-Z]", "", text)
        return stripped.upper()


    def set_key(self,new_key:str):
        self.__init__(new_key)


    def __pad(self,text:str,n:int):
        need_pad = -len(text)%n
        letters = string.ascii_uppercase
        pad = "".join(random.choices(letters,k=need_pad))
        return text+pad


    def encrypt(self,text:str):
        if isinstance(text,str)==False:
            raise TypeError('Input should be string')
        text = self.__encode(text)
        text = self.__pad(text,n=self.n)
        cipher = []
        text_list = list(text)
        for i in range(0,len(text_list),self.n):
            cipher+=[text_list[i + self.__key_order.index(x)] for x in range(self.n)]
        return "".join(cipher),self.__key_order


    def decrypt(self,text:str,key:str):
        if isinstance(text,str)==False:
            raise TypeError('Input should be string')
        if len(text)%self.n!=0:
            raise Exception("The length of input should be a mutiple of {}".format(self.n))
        if text.isalpha() == False:
            raise Exception("Invalid ciphertext: input contains non-alphabet characters")
        text_list = list(text)
        plain_text = []
        for i in range(0,len(text_list),self.n):
            plain_text+=[text_list[i + self.__key_order[x]] for x in range(self.n)]
        return "".join(plain_text)



