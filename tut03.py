set1 = {1,1,2,6,3}
a= set1 &{1,2}
print(a)
print(set1)
# ------------------
# strings

s = "0123456789"
print(s)
print(s[::-1])
print(s[:])

a = "  masala Chai  "
print(a.upper()) 
print(a.strip())
b = a.replace("Chai", "tea")
print(b)
print(a)

chai = "lemon, ginger, Masala, Mint"
print(chai.split())
print(chai.split(","))

chai = "Masala Chai"
print(chai.find("chai"))

chai = "Lemon Tea Tea Tea Tea"
print(chai.count("Tea"))

chai_type = "lemon"
quantity = 2

ch = "I ordered {}  cups of {} tea"
print(ch.format(quantity,chai_type))

ch = ["lemon","ginger","masala"]
print(ch)
print(" ".join(ch))
print("-".join(ch))

print(len(chai))

for letter in chai :
     print(letter)

