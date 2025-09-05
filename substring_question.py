s = "abcabcbb"
print(len(s))
# method 1
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substring = s[i:j]
        # if len(substring) == len(set(substring)):
        print(substring)


# chcek for repeadted character if it find then stop other goes 

# ---------------------------method2 --------------------
s = "abcabcbb"
left = 0
right = 0
n = len(s)
hashset = set()
max_length = 0
# <
# move right untill you find the repaeted character
# remove character using left pointer
# chcek right - left 
while right<n:
    if(s[right] not in hashset):
        hashset.add(s[right])
        right+=1
        max_length = max(max_length,right-left)
    else:
        hashset.remove(s[left])
        left+=1
print(max_length)


# ------------------------------------
# Longest Repeating Character Replacement

    