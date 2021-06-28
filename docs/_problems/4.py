# Create Phone Number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def list_to_str(l):
	result = ''
	index = 0
	while index < len(l):
		result += str(l[index])
		index += 1
	return result

def create_phone_number(n):
    return f'({list_to_str(n[:3])}) {list_to_str(n[3:6])}-{list_to_str(n[-4:])}'
	
assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
assert create_phone_number([0, 9, 7, 5, 5, 5, 2, 1, 1, 2]) == "(097) 555-2112"