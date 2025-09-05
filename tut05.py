chai_types = {"Masala":"Spicy", "Ginger":"zesty","Green":"mild"}
print(chai_types["Masala"])


chai_types["Green"]="Fresh"

print(chai_types)

for chai in chai_types:
    print(chai , chai_types[chai])
    

for chai , value in chai_types.items():
    print(chai,value)


if "Masala" in chai_types:
    print("yes")

print(len(chai_types))

chai_types["Early_Grey"] = "Citrus"
print(chai_types)

chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types["Green"]

print(chai_types)

copy = chai_types.copy()

tea ={
    "chai":{"Masala":"Spicy","Ginger":"zesty"},
    "Tea":{"Green":"mild","Black":"strong"}
}

print(tea)
tea = tea.clear
print(tea)


keys=["Masala","Ginger","lemon"]
default_Val = "Delicious"

data = dict.fromkeys(keys,default_Val)
