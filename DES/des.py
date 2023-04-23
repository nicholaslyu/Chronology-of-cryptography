IP_tb=[58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17,  9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7 ]

inv_IP_tb=[40, 8, 48, 16, 56, 24, 64, 32,
               39,  7, 47, 15, 55, 23, 63, 31,
               38,  6, 46, 14, 54, 22, 62, 30,
               37,  5, 45, 13, 53, 21, 61, 29,
              36,  4, 44, 12, 52, 20, 60, 28,
               35,  3, 43, 11, 51, 19, 59, 27,
               34,  2, 42, 10, 50, 18, 58, 26,
               33,  1, 41,  9, 49, 17, 57, 25 ]

permu_key_tb1=[ 57, 49, 41, 33, 25, 17,  9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11,  3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14,  6, 61, 53, 45, 37, 29,
               21, 13,  5, 28, 20, 12, 4 ]

permu_key_round=[ 14, 17, 11, 24,  1,  5,
               3, 28, 15,  6, 21, 10,
              23, 19, 12,  4, 26,  8,
              16,  7, 27, 20, 13,  2,
              41, 52, 31, 37, 47, 55,
              30, 40, 51, 45, 33, 48,
              44, 49, 39, 56, 34, 53,
              46, 42, 50, 36, 29, 32 ]

shift_1_step = set(0,1,8,15)
  



class DES:
    def __init__():
        self.keys = [0 for i in range(16)]
    
    # initial permutation based on IP_tb
    def IP(self,msg):
        temp_array = [0 for i in range(64)]
        for i in range(64):
              temp_array[i] = msg[IP_tb[i]-1]
        return tmp

    def IP_inv(self,msg):
        temp_array = [0 for i in range(64)]
        for i in range(64):
              temp_array[i] = msg[inv_IP_tb[i]-1]
        return temp_array
    
    # shift elements in the input list x step left 
    def shift_bits(self,input,step):
        right = l[step:]
        left = l[:step]
        return right+left

    def key_permu_initial(self,key):
        # 64 bits to 56 bits
        key_initial = [0 for i in range(56)]
        for i in range(56):
            key_initial[i] = key[permu_key_tb1[i]-1]
        return key_initial

    def key_permu_round(self,key):
        key_temp = [0 for i in range(48)]
        for i in range(48):
            key_temp[i] = key[permu_key_round[i]-1]
        return key_temp

    
    def key_schedule_all(self,key):
        key_0 = self.key_permu_initial(key)


        # 16 rounds
        for i in range(16):

            if i in shift_1_step:
                shift = 1
            else:
                shift = 2
            left = self.shift_bits(key_0[:28], step)
            right = self.shift_bits(key_0[28:], step)
            key_0 = left+right

            key_ith_round = self.key_permu_round(key0)
            self.keys[i] = key_ith_round
            
        return self.keys









    
    

    






