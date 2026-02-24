from typing import List
class day4_sliding_window:
    def max_Pr(self,nums:list[int])->int:
        minimum=float("inf")
        maximum=0
        for i in nums:
            minmum=min(minimum,i)
            maximum=max(maximum,i-minimum)
        return maximum
    
    def encode(self,strs: list[str]) -> str:
        message=''
        for i in strs:
            message+=str(len(i))+'#'+i

        return message

    def decode(self,s: str) -> list[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            legnth=int(s[i:j])
            j+=1
            word=s[j:j+legnth]
            decoded.append(word)
            i=j+legnth
        return decoded
if __name__=='__main__':
    solver=day4_sliding_window()
    encoded=solver.encode(["Hello","world"])
    print("Chypertest=",encoded)
    print("Original message=",solver.decode(encoded))
    
    print(solver.max_Pr([4,3,2,1,6,7,8,9,11]))
