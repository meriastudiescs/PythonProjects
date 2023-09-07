print("Welcome to the tip calculator!")
total = float(input("What was the total bill?\n$ "))
tip = int(input("What percentage tip would you like to leave? 10, 12, or 15?\n% "))
people = int(input("How many people to split the bill?\nP "))

total_bill = tip / 100 * total + total
each = total_bill / people
final_amount = "{:.2f}".format(each)
 
print(f"Each person should pay: ${final_amount}")