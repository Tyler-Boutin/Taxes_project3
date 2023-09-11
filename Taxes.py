#Income/marital status
earned_income = float(input("Enter your earned income : $"))
marital_status = input("Enter your marital status (S or M): ")

#Tax Brackets and Rates
single_brackets = [(0, 11000), (11001, 44725), (44726, 95375)]
married_brackets = [(0, 22000), (22011, 89450), (89451, 190750)]

#tax rates
tax_rates = [0.10, 0.12, 0.22]

#taxes based on marital status
if marital_status == "S":
	brackets = single_brackets
elif marital_status == "M":
	brackets = married_brackets
else:
	print("invlaid marital status. Please enter S (for single) or M (for married).")
	exit()

#tax owed
tax_owed = 0

for start, end in brackets:
	if earned_income <= start:
		continue
	elif earned_income <= end:
		taxable_amount = earned_income - start
	else:
		taxable_amount = end - start
	tax_owed += taxable_amount * tax_rates[brackets.index((start, end))]

#print taxes owed
print(f"Tax owed for {marital_status} filters with an income of ${earned_income:,.2f} in 2023 is ${tax_owed:,.2f}")
