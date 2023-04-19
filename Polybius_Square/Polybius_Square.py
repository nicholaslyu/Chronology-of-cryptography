ciphers = ["AA","AD","AF","AG","AV","AX",
           "DA","DD","DF","DG","DV","DX",
           "FA","FD","FF","FG","FV","FX",
           "GA","GD","GF","GG","GV","GX",
           "VA","VD","VF","VG","VV","VX"
           "XA","XD","XF","XG","XV","XX"]
letters = ["A","B","C","D","E","F","G","H"
           "I","J","K","L","M","N","O","P",
           "Q","R","S","T","U","V","W","X",
           "Y","Z","0","1","2","3","4","5",
           "6","7","8","9"]
import random
from re import sub

class ADFGVX:
    def __init__(self) -> None:
        random.shuffle(letters)
        self.key_decrypt = {ciphers[i]: letters[i] for i in range(len(letters))}
        self.key_encrpt = {letters[i]: ciphers[i] for i in range(len(letters))}

    def set_new_key(self):
        self.__init__()
    
    def encrypt(self,text:str):
        stripped = sub(r"[^a-zA-Z]", "", text)
        uppered = stripped.upper()
        return "".join([self.key_encrpt[char] for char in uppered])
    def decrypt(self,text:str):
         if not text.isalpha():
            raise Exception("Invalid input!")
         text = text.upper()
         return "".join([self.key_decrypt[text[i:i+2]] for i in range(0,len(text),2)])
    def show_key(self):
        print(self.key_encrpt)

        
