print("!! Welcome to the Tip Calculator !!")
bill = int(input("What was the total Bill: "))
rate = int (input("How Much tip you would like to give ? 10 12 or 15 ?? : "))
people = int(input("How Many people to split the bill ? : "))

rate = rate/100
final_bill = bill*(1+rate)

per_person = final_bill/people

final_amount = round(per_person,2)
print(f"your total bil is : {final_bill} and Each Person Should Pay : ${final_amount}")