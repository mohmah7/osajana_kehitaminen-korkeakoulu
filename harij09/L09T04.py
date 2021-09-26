first_name = raw_input('Anna etunimi:')
last_name = raw_input('Anna sukunimi:')

first_letter =''
second_name=''
number=1

for item in first_name:
	first_letter = first_letter+first_name[0]

for item in last_name:
	second_name = second_name+  last_name[len(last_name)-number]
	number+=1

print(first_letter)
print(second_name)