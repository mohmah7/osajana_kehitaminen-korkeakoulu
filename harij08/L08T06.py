first_number = input("Please insert year:")

second_number = first_number % 4

if second_number != 0:
	print("It is not leap year.")

if second_number == 0:
	print("It is leap year!")