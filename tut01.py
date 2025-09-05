from practice1 import greeting 

# greeting("hello aayush")
# l =[1,2,3,4]
# b = l
# print(b)
# print(id(l))
# print(id(b))
# print(b is l)
# b[0] = 100
# print(b)
# print(l)
# l[0]=200
# print(b)
# print(l)


l1 = [1,2,3,4]
l2 = l1
print(l1 is l2)
print(l1 == l2)
print(id(l1))
print(id(l2))
l1 = "hello world"
l1=[1,2,3,4]
l1[0]=100
print(l1)
print(l2)
print(id(l1))
print(id(l2))
# True, both lists have the same content
# True, both refer to the same list object

