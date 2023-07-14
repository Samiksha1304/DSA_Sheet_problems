def findDuplicate(arr):
    for i in range(0,len(arr)):
        if(arr.count(arr[i])==2):
            return arr[i]