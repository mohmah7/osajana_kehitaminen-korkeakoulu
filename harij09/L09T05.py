import random
number_list = []
number = 0

new_number =0

while len(number_list) <7:
	new_number = random.randrange(0,40)
	if new_number in number_list:
		#number -=1
		new_number =0
	else:
		number_list.append(new_number)
		#number +=1

number_list.sort()
print(number_list)