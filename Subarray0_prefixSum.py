class Solution:
    
    def subArrayExists(self,arr,n):
        
        prefix_sum = 0
        prefix_sums = set()

        for element in arr:
            prefix_sum += element
            if prefix_sum == 0 or prefix_sum in prefix_sums:
                return True
            prefix_sums.add(prefix_sum)

        return False
                

def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends