def make_hello(name):
	if name == "Петя":
		return name + ', я не знаю тебе'
	else:
		return 'Hello ' + name

print( make_hello('Вася') )
print( make_hello('Петя') )
