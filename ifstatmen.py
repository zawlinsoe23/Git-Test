x = int(input("please enter an integer"))
	#This is user input.
if x < 0:
	x = 0
	print ('Negative change to zero')
elif x == 0:
	print('zero')
elif x == 1:
	print('Single')
else:
	print('More')
# ingt - integer (Number)
# str - string (character)
# boolean - True , False
# float - 0.02, 0.5, 0.1

#comment
x = int(input("Please enter an integer"))
if x < 5:
	x = 0
	print ('x is small than 5')
elif x > 10:
	print ('x is bigger than 10')
elif x == 7:
	print('X is equal to 7')	
elif x > 5 and x < 10:
	print('x is between 5 & 10')
else:
	print ('X is underfined')


# 1 - 18
#19 - 50
#50 - 75

x = int(input("Please enter an integer"))
if x < 19:
	x = 1
	print ('go to School')
elif x > 18 and x <= 50:
	print ('go to Beach')
elif x > 50 and x <= 75:
	print ('go to Home')
else:
	print ('X is underfined')


print("I told that I don't like it")


words = ['cat', 'windows', 'degenestrate']
for w in words:
	print(w, len(w))


fruits = ['apple', 'banana', 'cucumber', 'pineapple', 'orange']
for f in fruits:
	print(f, len(w))

for i in range(5):
	print(i)
