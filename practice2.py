# # print("hello")
# # count =0
# # numbers = [1,3,-2,4,9,-1,4,-4]
# # for x in numbers:
# #     if(x<0):
# #         count+=1   

# # print("negative number is :",count)
# # print("positive number is",len(numbers)-count)


# # # even number sum :
# # def even_Sum(n):
# #     return n*(n+1)
# # print(even_Sum(10))

# # even_Number_Sum=0
# # n = 10
# # for i in range(1,n+1):
# #     if(i%2==0):
# #         even_Number_Sum+=1
# # print(even_Number_Sum)

# # # -----------------------
# # # table print
# # n = int(input("Enter the number you want to print the table :"))
# # for i in  range (1,11):
# #     if i==5:
# #         continue
# #     else :
# #         print(n,"x",i, " = ",n*i)
    
# # # Reverse a String 
# # string = "Today will be a good day "
# # print("original String: ",string)
# # reverse =""
# # for char in string :
# #      reverse=char + reverse
# # print(reverse)


# # 1st nonreepated char 
# input_string = "teetercards"
# for char in input_string:
#     if input_string.count(char)==1:
#         print("The Character is :",char)
#         break


# number = int(input("Enter the number you want factorial of these :"))
# i = 1
# while(number>0):
#     i=i*number
#     number-=1
    

# print(i)

# while True:
#     number = int(input("Enter the value b/w 1 and 10"))
#     if 1<= number <=10:
#         print("Thanks!")
#         break
#     else :
#         print("Invalid number try again !!")
        
# # prime number chcek
# number = int(input("Enter a number to check if it is prime: "))
# is_prime = True
# for i in range(2, int(number**0.5) + 1):
#     if number % i == 0:
#         is_prime = False
#         break
# print(f"{number} is {'a prime number' if is_prime else 'not a prime number'}.")


# # check Duplicate in list
# items = ["apple", "banana", "orange", "apple", "kiwi","kiwi"]
# unique_items = set()

# for item in items:
#     if item in unique_items:
#         print("Duplicate item s : ",item )
#     else :
#         unique_items.add(item)

# # Expopnential Backoff
# import time 

# wait_time = 1
# max_tries = 5
# attempts = 0

# while attempts<max_tries:
#     print("attempt : ",attempts+1,"- wait time ",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1
    
    
import math 

def circleStats(radius):
    area = math.pi * radius**2
    circumference = 2*math.pi*radius
    diameter = 2*radius
    return area,circumference,diameter

a,c,d = circleStats(5)
print("Area",round(a,2),"Circumference",round(c,2),"Diameter",round(d,2))

# Greet
def greeting(name = "User"):
    return f"Hello, {name}!"

print(greeting("komendra"))