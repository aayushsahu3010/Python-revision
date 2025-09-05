# nums = [3,4,6,1,2]
# previous_prod = [1]
# next_product=[1]



# # left_to_Right.insert(0,24)
# # left_to_Right.insert(0,14)
# # print(nums[len(nums)-1])
# n = len(nums)
# for i in range(1,n):
#     previous_prod.append(previous_prod[i-1]*nums[i-1])

# for i in range(n-2,-1,-1):
#     val = next_product[n-i-2]*nums[i+1]
#     next_product.append(val)
# next_product = next_product[::-1]

# for i in range(n):
#     nums[i]=previous_prod[i]*next_product[i]
# print(nums)
    
    



# print(next_product) 
# print(previous_prod)


# heights = [1,1]
# area =0

# i = 0
# j = len(heights)-1

# while i<j:
#     height= min(heights[i],heights[j])
#     width = j-i
#     area = max(area,height*width)
#     if heights[i] < heights[j]:
#         i+=1
#     else:
#         j-=1
# print(area)

# ------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


