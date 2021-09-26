#number = input('please enter number:')
numbers=[]
sum=0
while True:
	

	try:
		number = input('please enter number:')
		numbers.append(number)
		
	except:
		#print('hello')
		print('Lukujen anettu',len(numbers))
		for item in numbers:
			sum+=item
		print('sum is :',sum)
		exit()
