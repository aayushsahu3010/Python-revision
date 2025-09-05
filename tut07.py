# lambda function 
def add(a,b):
    return a+b

print(add(2,3))

print((lambda x:x**3)(3))

# args function 

def sum_all(*args):
    print("Arguments received:", args)
    for i in args:
        print(i, end=" ")
    return sum(args)

print(sum_all(1,2,3,4,5))

# key-value pair recive in function :

def print_info(**kwargs):
    print("Keyword arguments received:", kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_info(Name="Aayush", age=25, city="Delhi")
print_info(Name="Aayush", age=25, city="mp", country="India")
print_info(Name = "Shaktiman",power = "lazer",enemy = "Dr.jackal")


# yield function 
def even_number_gernation(num):
    for i in range(2,num+1,2):
        yield i
        
for i in even_number_gernation(20):
    print(i,end=" ")
        
print(list(even_number_gernation(20)))

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))