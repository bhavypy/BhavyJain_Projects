# import modules
import string
import random


# store all characters in lists
def strings():
	q=input("do you want to add alphabet in paas wd yes no??")
	if q=="yes":
		s1 = list(string.ascii_lowercase)
		s2 = list(string.ascii_uppercase)
		return s1,s2
strings()

def digi():
	q=input("Do You want to add digit in pass yes no?")
	if q=="yes":
		s3 = list(string.digits)
	return s3
digi()
def special():
	q=input("do you want add special charachter in pass yes no?")
	if q=="yes":
		s4 = list(string.punctuation)
	return s4
special()










# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# check this input is it number? is it more than 8?
while True:

	try:

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break

	except:

		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])


# shuffle result
random.shuffle(result)


# join result
password = "".join(result)
print("Strong Password: ", password)
