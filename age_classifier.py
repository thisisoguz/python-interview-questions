age = int(input("Please specify an age: "))

if age <= 0:
	print("There is something wrong about the age. Please double check it!")
elif age >= 0 and age < 20:
	print("The person is underaged.")
elif age >= 20 and age < 40:
	print("The person is young.")
else:
	print("The person is boomer.")