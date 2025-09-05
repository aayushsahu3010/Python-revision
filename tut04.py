varities = ["Black","Green","Oolong","white"]
print(varities[::-1])
print(varities)

print(varities[1:1])
varities[1:1]=["test","test"]
print(varities)


print(varities[1:2])
varities[1:2] = ["aayush"]
print(varities)

varities[1:3]=[]
print(varities)

for tea in varities:
    print(tea,end="-",sep="#")

varities.append("Masala")
print(varities)

varities.remove("Green")
print(varities)

varities.insert(1,["lemon","ginger"])
print(varities)

tea_varities = varities[:]
print(tea_varities)
print(varities)
print(tea_varities is varities)


varities_copy= varities.copy()
print(varities_copy)
print(varities_copy is varities)

tea_varities.append("aayush")
print(varities)
print(tea_varities)

varities_copy.append("lemon")
print(varities_copy)


# list Comprehensino
square = [x**2 for x in range(10)]
print(square)

y = range(10)
print(y)