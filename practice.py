list = [1, 2, 3, 4, 5, 1]


# def func(list, tagret):
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] + list[j] == target:
#                 print(f"{i} the elememnt {list[i]} {j} th element {list[j]} ")


# # func(lis

# mask = 1


# a = 10
# print(bin(a))
# print(len(bin(a)))

# n = 10  # 1010
# bits = n.bit_length()  # number of bits needed

# for i in range(bits):
#     if n & (1 << i):
#         print(f"Bit {i}: SET (1)")
#     else:
#         print(f"Bit {i}: UNSET (0)")

# # bit manipulation
# n = 10  # 1010
# mask = 1

# print(n & 1 << 2)  # left shift
# print(n >> 1)  # right shift


l = [10000, 9999, 9998, 1, 9650, 9649, 9648, 9647, 9646]
profit = 0
# print(len(l))
# for i in range (len(l)):
#     buy  = l[i]
#     for j in range(i+1,len(l)):
#         diff = (l[j]-buy)
#         profit =max(diff, profit)
#         print(f"when i purchase on {buy} and sell it on day {l[j]} then the profit  is {profit} the and the difference is {diff}")


# print(profit)
# print(l.index(9646))


# buy_price =l[0]
# current_profit = 0
# max_profit = 0
# for item in l:
#     if(buy_price>item):
#         buy_price = item

#     if(item>buy_price):
#         current_profit = item-buy_price
#         max_profit = max(current_profit,max_profit)

# print(max_profit)


# def binary_search(nums, low, high, target):
#     while low < high:
#         mid = int((low + high) / 2)
#         if nums[mid] == target:
#             return mid
#         elif nums[low] < nums[mid]:
#             low = mid + 1
#         elif nums[mid] < nums[high]:
#             high = mid - 1
#     return -1


# nums = [1, 3]
# target = 1
# pivot = 0
# low = 0
# high = len(nums) - 1
# while low <= high:
#     mid = int((low + high) / 2)
#     if nums[low] < nums[mid]:
#         low = mid + 1
#         if nums[low] < nums[high]:
#             pivot = low

#     else:
#         high = mid - 1
#         if nums[low] < nums[high]:
#             pivot = low

# print(pivot)
# if nums[pivot] == target:
#     print(pivot)

# elif target >= nums[pivot] and target <= nums[len(nums) - 1]:
#     print(binary_search(nums, pivot, len(nums) - 1, target))
# else:
#     print(binary_search(nums, 0, pivot - 1, target))


# # [1,3] target = 3,return 1
# # low = 0
# # high = len(nums)-1
# # while(low<=high):
# #     mid = int((low+high)/2)
# #     print("loop start")
# #     if(nums[mid]==target):
# #         print(mid)
# #         break
# #     elif(nums[low]<nums[mid]):
# #         low = mid+1
# #     elif(nums[mid]<nums[high]):
# #         high = mid-1


# def set_bits(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count

# a = 5
# count = 0
# b = a.bit_length()
# for i in range(b):
#     if a & (1 << i):
#        count+=1
# print(count)
# print(set_bits(a))
# print(1>>1)#decrease the value
# print(1<<1)#increase the value

# a = 43261596
# # reverse = a[::-1]
# # print(int(reverse,2))

# print(bin(43261596))
# # print(reverse)# Output: 11

# # print(a^a-1)
# def missingNumber(nums):
#     n = len(nums)
#     xor1 = 0
#     xor2 = 0
    
#     # XOR from 0 to n
#     for i in range(n+1):
#         xor1 ^= i
    
#     # XOR all array elements
#     for num in nums:
#         xor2 ^= num
    
#     return xor1 ^ xor2

# print(missingNumber([3,0,1]))  # Output: 2

# print(4>>1)

# def reverse_number(n):
#     rev = 0
#     for i in range(32):
#         bit = n&1
#         rev = (rev<<1)| bit
#         n=n>>1#right shift 
#     return rev

# print(reverse_number(2147483644))
# # 2147483644

# a =5
# # print(bin(a,'032b'))
# b=(f"{a:032b}")
# a = b[::-1]
# print(b)
# print(a)
# print(int(a,2))

# nums=[1,3,5,6]
# target = 5
# n = len(nums)-1
# def bianry_S(nums,low,high,target):
#     while(low<high):
#         mid = int((low+high)/2)
#         if(nums[mid]==target):
#             return mid
        
#         if(nums[mid]<target):
#             low = mid+1

#         if(nums[mid]>target):
#             high = mid-1
#     return low

# print(bianry_S(nums,0,n,2))  


# s = "A man, a plan, a canal: Panama"
# string=""
# for i in range(len(s)):
#             if(s[i].isalpha()):
#                 string+=s[i]
        
# print(string)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if(s==" "):
#             return True
#         s = s.lower()
#         string =" "
#         for i in range(len(s)):
#             if(s[i].isalpha()):
#                 string+=s[i]
        
#         print(string)
        
#         print(string[::-1])
#         if(string==string[::-1]):
#             return True
#         else:
#             return False
        
# a = Solution()
# print(a.isPalindrome(s))
# print(s[0].isalnum())

l=[1,2,3,4] #Output: [1,5,2,4,3]
a=[]
n=len(l)-1
for i in range((len(l)+1)//2):
    a.append(l[i])
    if(i!=n-i):
        a.append(l[n-i])
print(a)  
    

for i in range(len(l) // 2):
    l.insert(2 * i + 1, l.pop())
print(l)