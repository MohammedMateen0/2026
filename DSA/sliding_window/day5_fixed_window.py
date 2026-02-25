def char_incusion(s1:str,s2:str)->bool:
    if len(s1)>len(s2):
        return False
    freq1=[0]*26
    freq2=[0]*26
    for char in s1:
        freq1[ord(char)-ord('a')]+=1
    for i in range(len(s1)):
        freq2[ord(s2[i])-ord('a')]+=1
    if freq1==freq2:
        return True
    left=0
    for right in range(len(s1),len(s2)):
        freq2[ord(s2[right])-ord('a')]+=1
        freq2[ord(s2[left])-ord('a')]-=1
        left+=1
        if freq1==freq2:
            return True
    return False
char_incusion('ab','absed')        