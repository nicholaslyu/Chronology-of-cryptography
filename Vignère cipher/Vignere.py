from re import sub
from itertools import cycle

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

class Vignere:
    def __init__(self,key:str):
        self.key = key.upper()
        self.key_list = [sub_encrpty[char] for char in self.key]

    def encrypt(self,msg:str):
        if not msg.isalpha():
            raise Exception("Invalid input!")
        stripped = sub(r"[^a-zA-Z]", "", msg)
        to_nums = [sub_encrpty[char] for char in stripped]
        shifted = [(x + shift) % 26 for x, shift in zip(to_nums, cycle(self.key_list))]
        to_string = "".join([sub_decrypt[char] for char in shifted])
        return to_string
    
    def decrypt(self,msg:str):
        if not msg.isalpha():
            raise Exception("Invalid input!")
        msg = msg.upper()
        to_nums = [sub_decrypt[char] for char in msg]
        shifted =  [(x - shift) % 26 for x, shift in zip(to_nums, cycle(self.key_list))]
        to_string = "".join([sub_decrypt[char] for char in shifted])
        return to_string
    
    def set_key(self,key:str):
        self.__init__(key)


        

