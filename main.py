#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line

print("Welcome to Oumar's Bill and Tip Calculator!")

bill = float(input("What was the total bill? £"))

tip = int(input("How much tip (percent) would you like to give? (only enter the number)"))

people = int(input("How many people to split the bill between?"))

tip_percent = (tip / 100)

total_bill = (bill * (1 + tip_percent))

#per_person = round(total_bill / int_people, 2)
per_person = "{:.2f}".format(total_bill / people)

print(f"Each person should pay: £{per_person}")
