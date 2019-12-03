def my_max(a, b):
	if a > b:
		return a
	elif b > a:
		return b
	else:
		return 'equal'

m = my_max(3, 5)
print(m)
print( my_max(5,3) )
print( my_max(5,5) )