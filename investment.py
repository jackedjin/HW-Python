def calculate_apr():
"Calculates the compound interest of an initial investment of $500 for 65 years"
	principal=500
	interest_rate=0.03
	years=0

	while years<65:
	"while loop used to repeat the compounding effect of the investment 65 times"
		principal=principal*(1+interest_rate)
		print(f'After year {years}, the new principal is {principal}')
		years+=1
		"counter which automatically adds 1 into integer variable years until it reaches 65"
	print(f'On the {years}th year, the principal has become {principal}')
calculate_apr()
