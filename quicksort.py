def Quick_Sort(arr,low,high):
    if(low<high):
        pos = partition(arr,low,high)
        
        Quick_Sort(arr,low,pos-1)
        Quick_Sort(arr,pos+1,high)


def  partition(arr,low,high):
    pivot = arr[low]
    i, j = low, high

    
    while i<j:
        while (i<=high and arr[i]<=pivot):
            i+=1
        
        while(j>=low and arr[j]> pivot):
            j-=1
        
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]

    
    return j
    
    
       
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)
print("Sorted:  ", Quick_Sort(arr,0,len(arr)-1))