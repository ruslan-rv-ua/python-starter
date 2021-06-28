# Inverse Slicer
# https://www.codewars.com/kata/586ec0b8d098206cce001141

def inverse_slice(items, a, b):
    # Your code here.
	items[a:b] = []
	return items
	return items[:a] + items[b:]
	
assert inverse_slice([12, 14, 63, 72, 55, 24], 2, 4) == [12, 14, 55, 24]
assert inverse_slice([12, 14, 63, 72, 55, 24], 0, 3) == [72, 55, 24]
assert inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13) == ['Intuition', 'is', 'a', 'poor', 'guide']