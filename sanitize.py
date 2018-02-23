def make_lower( text ):
	if len(text) <= 0:
		return 'no input provided'
	return text.lower()

def make_capital( text ):
	if len(text) <= 0:
		return 'no input provided'
	return text.capitalize()

def make_number( input_value ):
	if input_value.isdigit():
		return int(input_value)
	return 'No number provided.'

def make_title( text ): 
	if len(text) <= 0:
		return 'no input provided'
	return text.title()