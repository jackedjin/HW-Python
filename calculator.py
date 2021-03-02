def input_output():
	'''
	prompts user to enter number1,number2 and the desired operator.
	calls the function calculator which takes in 3 parameters,
	calculates them based on the arithmetical operations coded within the function
	'''
	dec = 'y' "initialized string value to 'y'"
	oper = '' "initialized null string value"
	while dec=='y': "while loop until user enters n which breaks the loop"
		num1=input("Enter number1:")
		num1=int(num1)
		print(num1) 
		num2=input("Enter number2:")
		num2=int(num2)
		print(num2)
		oper=input("Enter operator:")
		print(oper)
		result=calculator(num1,num2,oper)
		'''
		calls and passes parameters to function calculator,
		and returns the result
		'''
		print(result)
		dec=input("Enter 'y' to continue or 'n' to exit:")
		if dec == 'n':
			break
def calculator(number1,number2,operator):
	'''
	determines the arithmetic operator with conditional if statements,
	and returns respective results
	'''
	if operator=='+':
		return number1+number2
	if operator=='-':
		return number1-number2
	if operator=='*':
		return number1*number2
	if operator=='/':
		return number1/number2
	if operator=='//':
		return number1//number2
	if operator=='**':
		return number1**number2
input_output()
