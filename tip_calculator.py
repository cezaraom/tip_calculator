print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = float(input("What the porcentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip/100 * bill + bill

resultado = bill_with_tip / people
final_amount = round(resultado, 2)
print(f"Each person should pay: ${final_amount}")
