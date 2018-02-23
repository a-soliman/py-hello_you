'''
 1. Ask user for name.
 2. Ask user for age.
 3. Ask user for city.
 4. Ask user what they enjoy

 5. Create output text.
 6. Print output to screen
'''

name 	= input('What is your name?: ')
age 	= int(input('How old are you?: '))
city 	= input('In which city do you live?: ')
hobies 	= input('What do you enjoy doing?: ') 

user = {
	'name': name, 
	'age': age,
	'city': city,
	'hobbies': hobies
}

