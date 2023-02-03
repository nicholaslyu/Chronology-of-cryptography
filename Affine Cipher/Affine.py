from re import sub
sub_encrpty = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,
       "H":7,"I":8,"J":9,"K":10,"L":11,"M":12,
       "N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,
       "T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,
       "Z":25}
sub_decrypt = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",
       7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",
       13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",
       19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",
       25:"Z"}
class Affine:
    def __init__(self,a:int,b:int) -> None:
        self.a = a
        self.b = b
        self.__inverse_a = self.__xgcd(a,26)[0]
    def __xgcd(self,a,b):
        if b ==0:
            return 1,0
        else:
            x,y = self.__xgcd(b,a%b)
            x,y = y,(x-(a//b)*y)
            return x,y
    def show_key(self):
        return self.a,self.b

    def __encode(self,text: str):
        stripped = sub(r"[^a-zA-Z]", "", text)
        return stripped.upper()

    def set_key(self,a:int,b:int):
        self.__init__(a,b)


    def encrypt(self,text:str):
        text = self.__encode(text)
        cipher = "".join([sub_decrypt[(self.a*sub_encrpty[letter]+self.b)%26] for letter in text])
        return cipher

    
    def decrypt(self,text:str):
        if text.isalpha()==False:
            raise Exception("Input should contain only alphbets")
        if text.isupper() == False:
            raise Exception("Input should be upper case letters")
        plain_text = "".join([sub_decrypt[self.__inverse_a*(sub_encrpty[letter]-self.b)%26] for letter in text])
        return plain_text
a = Affine(a=7,b=17)
d = a.encrypt("VYOHVUTWVHPZUWTZUUBEYDUB")
print(a.decrypt(d))


    
        


