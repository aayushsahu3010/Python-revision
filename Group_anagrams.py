from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = 0
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# method1 using sorti/ng method
# my_dict = defaultdict(list)
# for item in strs :
#     key = "".join(sorted(item))
#     my_dict[key].append(item)


# print(my_dict.values())

# method2 - categorize by frequency
# from collections import Counter

# s = "aabbc"  # a2b2c1
# freq = Counter(s)
# print(freq)
# dict = {}

# for i in range(len(s)):
#     dict[s[i]] = dict.get(s[i], 0) + 1
# print(dict)


# result = ""
# for ch in dict:
#     result += ch + str(freq[ch])

# print(result)


# def group_anagram(strs):
#     if strs == None or len(strs) == 0:
#         return list()


# group_anagram(strs)




# method 3
def anagramsgroup(strs):
    res = defaultdict(list)
    for s in strs:
        count=[0]*26
        
        for c in s:
            count[ord(c)- ord('a')]+=1
        res[tuple(count)].append(s)
    return (res)
val = anagramsgroup(strs)
print(val.keys())


# print(val)

print(ord('a'))