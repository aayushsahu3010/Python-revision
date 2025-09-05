# detail in numbers
result = 1/3.0
print(result)

a = "hello\nworld"
print(repr(a))


import random 
print(random.random())
print(random.randint(1,100))

l1 = ["lemon", "ginger", "mint"]
print(random.choice(l1))
random.shuffle(l1)
print(l1)

from decimal import Decimal
a = Decimal('0.1') +Decimal('0.2')
print(a)

from fractions import Fraction
b =Fraction(4,5)
print(b)