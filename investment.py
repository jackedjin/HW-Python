def calculate_apr():
	principal=input("Enter principal amount:")
	principal=int(principal)
	print(f'Your principal is {principal}')
	interest_rate=input("Enter interest rate:")
	interest_rate=int(interest_rate)
	print(f'Your interest rate is {interest_rate} percent')
	years=input("Enter number of years:")
	years=int(years)
	print(f'The number of years you selected is {years}')
	x=0

	while x<years:
		principal=principal*(1+interest_rate/100)
		print(f'After year {x}, the new principal is {principal}')
		x+=1
	print(f'On the {x}th year, the principal has become {principal}')
calculate_apr()
