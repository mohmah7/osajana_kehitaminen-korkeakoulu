def check_int(number):
	if (number == 10) or (number == 20):
		print("Luku on 10 tai 20")
	elif (number == 100) or (number == 200):
		print("Luku on 100 tai 200")
	else:
		print(number)

	return 0

first_number = input("Please enter number:")

check_int(first_number)