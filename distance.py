#distance calculator

distance=int(input("How far you traveling? 'MPH'"))
x=int(input("How fast will you be traveling? 'MPH'"))

time= distance / x

print("At",x,"MPH you will arrive at your destination in",time,"hours")

if time > 2: #checks time
	print("You have a long trip!")
else:
	print("You have a short trip!")