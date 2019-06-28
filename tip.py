meal_order = input(" your order: ")
meal = int(input("enter amount: "))
tip = float(0.08)
tax = float(0.05)
bill = (meal * tax)
total_bill =(bill + tip)

print("your bill: ", bill)
print("your total bill with tip: ",total_bill)

