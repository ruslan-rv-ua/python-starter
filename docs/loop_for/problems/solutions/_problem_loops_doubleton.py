'''
"��������"

������ �������� ���������� ���������� �����, ��� ���������� � ������������� ���� ���� ����� ����.
��������� �����-���������: 23, 35, 100, 12121.
�� ���������: 123, 9980.
��������� ������� next_doubleton(num).
������� ������ ���������� ����� num.
������� ������� ��������� �����-�������� ����� �� num.
'''
# ��� ��� ���������� ���

# https://www.codewars.com/kata/604287495a72ae00131685c7
def is_doubleton(num):
	digits = [0] * 10
	for ch in str(num):
		digits[int(ch)] = 1
	return sum(digits) == 2
	
def next_doubleton(num):
	while True:
		num += 1
		if is_doubleton(num):
			return num

# ��� �����, �� ������ ��� ���
assert next_doubleton(120) == 121
assert next_doubleton(1234) == 1311
assert next_doubleton(10) == 12
assert next_doubleton(1) == 10
assert next_doubleton(111) == 112
