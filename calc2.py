active = True

opening = "~~~~~~~~~~~~~~~~~~~~~~~~"
opening += "Hellow and Welcome!"
opening += "Thank you for using this calculator! You can calculate the amount of time in months that you will acquire a given fund with your current hourly wage along with the hours you get. Would you like to get started? Y/N "
opening += "~~~~~~~~~~~~~~~~~~~~~~~~"

openResponse = input("\t")
print(opening)
print(openResponse)

if openResponse == "Y" or "y":
	wage = input("please enter your hourly wage: ")
	hours = input("please enter your total hours in one week (include overtime if applicable.")
	goal = input("What is your monetary goal that you'd like to achieve?")
	while True:
		expenses = []
		for expense in expenses:
			expense = input("Please enter an expense. If you do not have any (more) expenses, please type 'quit'.")
		if expense == 'quit':
			break
		elif expense != range(0, 100000):
			print("Invalid character, please try again.")
		else:
			


elif openResponse == "N" or "n":
	print("\nAre you sure you would like to quit? ")
	ifquit = input("\t")
	while ifquit != "Y" or "y" or "yes" or "Yes":
		break
else:
	print("Invalid character, please try again.")
