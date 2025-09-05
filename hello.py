
# print("hello home and hello world ")
# # \n
# print("hello world \n hello aayush")

# """
# hbhdifvbnnbihu huhuihaiuhdiubfhiuhhuuhu
# """

# _a = "hello"
# print(_a)

# name = "Aaha"
# age = 23
# print(type(23))
# print(type(name))

# print("hello my name is " + name + "i am ", age, "years  old")

# print(1, 2, 3, 4, 4, 5, 6, 6, sep="#,")
# print(12234567, sep="#,")
# print(123, end="#")
# print(1, 2, 3, 4, 5, end="#\n")


# # a-z : 97 to 122.
# # A-Z : 65 to 90.
# # 0 to 9 : 48 to 57.
# # SPACE : 32

# char = "@"
# c = "$"
# ch = "a"

# # ord - use to get ascii value of a character
# print(ord(ch))
# print(ord(char))
# print(ord(c))

# # chr -it can help to just opposite the ascii value
# print(chr(97))


# # input tag =
# name1 = input("enter your name :")
# print("your name is " + name1)

# print(int(3.13))
# print(int(3.89))
# print(float("123"))
# print(str(123))


# -----------------------------operators-------------------------
num1 = 23
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)
print(num1 // num2)
print(num1**num2)


# logical operator

exp1 = 3>5
exp2 = 5>4

print("exp1 and exp2", exp1 and exp2)
print("exp1 or exp2 ", exp1 or exp2)
print("not exp1", not exp1)

# identity operators
x = 12
y = "12"

# print(x is y ) -It does not compare values. Instead, it checks if both variables point to the exact same object in memory
print(x is not y )
print(x is int(y))
print(id(x))
print(id(y))
print(id(int(y)))

# membership operator in ,not in 

fruits = ["banana","apple","mango","kiwi"]
print("if kiwi is in fruits ? ", "kiwi" in fruits )
print("if orange  not in fruits ? ", "orange" not in fruits) 



'''
# bit wise operators (demo)
logical and - &
logical or - |
xor -^
Nor - ~
left shift - <<
right shift - >>'''

a = 5 
b = 3 
print(" a and b :", a&b)
print("a or b :",a|b)
print("a xor b :", a^b)
print( " nor of b :", ~b)
print("left shift of a : ",a<<1)
print("right shift of b : ",b>>2)


a1 = 12 
q2 = 24 
print ("is a1 is q1 ??",a1 is q2 )



print(int('0b1010',2) + int ('A',16))

print(bool("false")==False)

