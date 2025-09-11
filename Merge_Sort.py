
def merge_sort(arr):
    if (len(arr))<=1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    
    return merge(left_half,right_half)


def merge(arr1,arr2):
    result = []
    i,j=0,0
    
    while i<len(arr1) and j<len(arr2):
        if (arr1[i]<= arr2[j]):
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result 


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Original:", arr)
print("Sorted:  ", sorted_arr)