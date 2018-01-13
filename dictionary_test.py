#Branson = {'personality': 'gay', 'last name': 'Wolf', 'city': 'oceanside'}

#print("Branson is " + Branson['personality'].title())
#print("His last name is " + Branson['last name'])
#print("He lives in " + Branson['city'].title())

#print("\n")
friends = {
	'Branson': [5, 3, 10, 15],
	'Alex': [6, 26, 33, 14],
	'Connor': [13, 45, 98, 47],
	'Reb': [17, 2, 84, 93],
	}

for friend, numbers in friends.items():
	print(friend + "'s favorite numbers are: ")
	for number in numbers:
		print(number)

print("\n")











#user0 = {
#	"Username": "Nosty",
#	"First Name": "Branson",
#	"Last Name": "Wolf",
#}

#for key, value in user0.items():
#	print("\nKey: " + key)
#	print("Value: " + value)

words = {
	"watermelon": "fruit",
	"house": "construction",
	"mountain": "Earth",
}

for key, value in words.items():
	print(key.title() + " is to " + value.title())

print("\n")

#~~~~~~~~~~~~~~~~~~~~
rivers = {
	"Nile": "Egypt",
	"Ganges": "India",
	"Yangtze": "China",
	"Danube": "Europe",
}
for rivers, location in rivers.items():
	print("The " + rivers.title() + " runs through " + location.title())
	#~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
#	'erin': 'C++'
}

print("\n")
for key, value in set(favorite_languages.items()):
	print(key.title() + "'s favorite language is " +
		value.title() + ".")
if 'erin' not in favorite_languages.keys():
	print('erin, please take the poll!')