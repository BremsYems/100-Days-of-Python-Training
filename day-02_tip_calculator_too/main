#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Brendan's tip calculation tool! I live in SG and we don't HAVE to do that here, so this one's mostly for you, American brothers!")

whole_bill = float(input("The total bill was: $"))
tip_percentage = float(input("Please select a percentage to tip (%) 0, 10, 12, 15: "))
no_to_split_bill = int(input("Thank you. Kindly select the number of patrons splitting the bill tonight: "))

final_bill = (whole_bill * (1 + (tip_percentage / 100))) / no_to_split_bill

# .2f is to round to 2 decimal places
print(f"Each person should pay: ${final_bill:.2f}")
