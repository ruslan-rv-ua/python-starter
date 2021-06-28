# Double Every Other
# https://www.codewars.com/kata/5809c661f15835266900010a

def double_every_other(lst):
	for i in range(1, len(lst), 2):
		lst[i] *= 2
	return lst
	
assert double_every_other([1,2,3,4,5]) == [1,4,3,8,5]
assert double_every_other([1,19,6,2,12,-3]) == [1,38,6,4,12,-6]
assert double_every_other([-1000,1653,210,0,1]) == [-1000,3306,210,0,1]