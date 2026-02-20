from typing import List
import heapq
class Day2Patterns:
    
    def group_anagrams(self,strs:list[str])->list[list[str]]:
        groups={}
        for word in strs:
            count=[0]*26
            for i in word:
                index=ord(i)-ord('a')
                count[index]+=1
            key=tuple(count)
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
    
    def k_frequent(self,nums:list[int],k:int)->list[int]:
        counts={}
        result=[]
        for i in nums:
            counts[i]=counts.get(i,0)+1
        sorte=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    
        for i in range(k):
            result.append(list(sorte)[i][0])
        return result
    
    def top_k_frequent(nums:list[int],k:int)->list[int]:
        count={}
        heap=[]
        result=[]
    
        for i in nums:
            count[i]=count.get(i,0)+1
        for key,freq in count.items():
            heapq.heappush(heap,(-freq,key))
            
        for i in range(k):
            freq,top=heapq.heappop(heap)
            result.append(top)
        return result
    
    def length_of_longest_substring(s:str)->int:
        char_set=set()
        max_legth=0
        left=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_legth=max(max_legth,right-left+1)
        return max_legth

    
if __name__=="__main__":
    solver=Day2Patterns()
    print(solver.top_k_frequent([1,1,1,2,2,3,3,3,4,4,4,4,4],2))  
    print(solver.k_frequent([1,1,1,2,2,2,2,3,3],3))
    print(solver.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solver.length_of_longest_substring("abgsdtrs"))
  