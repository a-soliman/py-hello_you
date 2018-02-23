'''
 1. Ask user for name.
 2. Ask user for age.
 3. Ask user for city.
 4. Ask user what they enjoy

 5. Create output text.
 6. Print output to screen
'''

from person_class import *
from sanitize import *

name 	= input('What is your name?: ')
name 	= make_lower(name)
name 	= make_title(name)

age 	= int(input('How old are you?: '))

city 	= input('In which city do you live?: ')
city	= make_title(city)

hobbies = input('What do you enjoy doing?: ') 
hobbies	= make_capital(hobbies)

new_person = Person(name, age, city, hobbies)
print(new_person.get_user_info())