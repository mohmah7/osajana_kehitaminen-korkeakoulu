balance = 2000.0
usr_input_third = 0.0
print("Bank account balance is",balance, "euros")
usr_input_first = input("How many euros will be added to the balane?")
usr_input_second = input("How many cents will be added to the balance?")
usr_input_second = usr_input_second+usr_input_third
usr_input_second = usr_input_second/100 
#print(type(usr_input_second))
print("Bank account balance :", balance+usr_input_first+usr_input_second, " euros")
