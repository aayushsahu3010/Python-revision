# # Age Group
# age = int(input("Enter Your Age: "))
# if(age<13):
#     print("you are a Child ")
# elif( age<=19):
#     print("you are a teenager")
# elif(age<60):
#     print("you are under the category of Adult")
# else:
#     print("you are under the senior section ")

# # ----------------------------
# wednesday = False

# price = 12 if age>=18 else 8

# if wednesday :
#     price = price - 2

# msg = "your age is {} years old and  movie ticket price is {}"
# print(msg.format(age,price))

# # -------------------------------
# # Grade Calculator
# score = int(input("Enter your score: "))

# if(score>=101):
#     print("Invalid Score")
#     exit()

# if(score>=90):
#     grade = "A+"


# # weather activity
# activity = "Stay Home"
# weather = input("Enter the weather (sunny/rainy/snowy): ").lower()
# if weather =="sunny":
#     activity = "Go for a walk"
# elif weather=="Rainy":
#     activity = "Read a Book"
# elif weather =="Snowy":
#     activity = "Build a Snowman"

# print(activity)

# # ---------------------------------

distance = int(input("Enter the distance (in km) :"))
if distance < 3:
    print("you can take a bicycle")

elif distance <= 15:
    print("you can take a bike")
else:
    print("you can take a car ")

# --------------------------------
# leap Year Program
year = int(input("Enter the year"))

if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print("The year is a leap year")
else:
    print("year is not a leap year")
