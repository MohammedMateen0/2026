def is_anagram(s:str,t:str)->bool:
    count1,count2={},{}

    if len(s)==len(t):
        for cher in s:
            count1[cher]=count1.get(cher,0)+1
        for cher in t:
            count2[cher]=count2.get(cher,0)+1
        if count1 == count2:
            return True
    return False
print(is_anagram("anagram","nagaram"))
