# Count of positives / sum of negatives
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
	if len(arr) == 0:
		return []
	positives_count = 0
	sum_negatives = 0
	for i in arr:
		if i > 0:
			positives_count += 1
		if i < 0:
			sum_negatives += i
	return [positives_count, sum_negatives]
	
assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10,-65]
assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8,-50]
assert count_positives_sum_negatives([1]) == [1,0]
assert count_positives_sum_negatives([-1]) == [0,-1]
assert count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]) == [0,0]
assert count_positives_sum_negatives([]) == []
