import math

def solution(str1, str2):
    str1_set = []
    str2_set = []
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2:
        return 65536
    
    elif len(str1) == 0 and len(str2) == 0:
        return 0
    else:
        for i in range(len(str1)-1):
            if str1[i:i+2].isalpha():
                str1_set.append(str1[i:i+2])
            
        for j in range(len(str2)-1):
            if str2[j:j+2].isalpha():
                str2_set.append(str2[j:j+2])

        print(str1_set)
        print(str2_set)
        
        # 합집합
        tmp = str1_set.copy()
        uni = str1_set.copy()
        
        for x in str2_set:
            if x not in tmp:
                uni.append(x)
            else:
                tmp.remove(x)
                
        # 교집합
        inter = []
        
        for y in str2_set:
            if y in str1_set:
                str1_set.remove(y)
                inter.append(y)
        
        print(inter)
        print(uni)
        
        return math.floor((len(inter) / len(uni))  * 65536)
    
    
    
    