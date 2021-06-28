# Достатньо!
# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    # code here
	result = []
	for e in order:
		if result.count(e) < max_e:
			result.append(e)
	return result
	
	
	
assert delete_nth([20,37,20,21], 1) == [20,37,21]
assert delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
assert delete_nth([1,1,1,1],2) == [1,1]
assert delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3) == [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
assert delete_nth([1,1,1,1,1], 5) == [1,1,1,1,1]
assert delete_nth([], 5) == []