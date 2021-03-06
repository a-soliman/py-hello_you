from sanitize import *

class Person:
	__name 		= ''
	__age		= 0
	__city		= ''
	__hobbies 	= ''

	# CONSTRUCTOR
	def __init__( self, name, age, city, hobbies ):
		self.__name 	= name
		self.__age 		= age
		self.__city		= city
		self.__hobbies	= hobbies


	# GETTERS
	def get_name( self ):
		return self.__name

	def get_age( self ):
		return self.__age

	def get_city( self ):
		return self.__city

	def get_hobbies( self ):
		return self.__hobbies

	
	# SETTERS
	def set_name( self, name ):
		self.__name = name
		return

	def set_age( self, age ):
		self.__age = int(age)
		return

	def set_city( self, city ):
		self.__city = city
		return

	def set_hobbies( self, hobbies ):
		self.__hobbies = hobbies
		return


	# OTHERS
	def get_user_info( self ):
		output = '{}, is {} Years old. Lives in {}, and Enjoys {}.'.format(self.__name, self.__age, self.__city, self.__hobbies)
		return output