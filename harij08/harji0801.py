def kerro3():
	age = input("Please enter age:")
	if age < 13:
		print("Child")
	elif (age <= 19) and (age>=13):
		print("Teen")
	elif (age <= 65) and (age >= 20):
		print("Adult")
	else :
		print("Senior")

kerro3()

