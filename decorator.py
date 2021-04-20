def displaydecorator(fn):
	def display_wrapper(message):
		print('Output:')
		fn(message)
	return display_wrapper
	
@displaydecorator
def display(message):
	print("Inner Function")
	print(message)
	
display("Hello")