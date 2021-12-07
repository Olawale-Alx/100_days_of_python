#Tip Generator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator')

total_bill = input('What was the total bill\n$')

tip = int(input('How many percent will you like to give as tip? 10, 12, or 15\n'))

total_bill = float(total_bill)
total_bill = total_bill + (total_bill * (tip / 100))

people = int(input('How many people to split the bill?\n'))

bill_per_person = total_bill / people
bill_per_person = round(bill_per_person, 2)

print(f'Each person should pay: ${bill_per_person}')
