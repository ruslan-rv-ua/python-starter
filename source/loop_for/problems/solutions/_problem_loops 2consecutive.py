'''
"��� ��������� �����"

��������� ������� is_there_consecutive.
������� ������ ���������� �����.
������� ������� True, ���� � ����������� ����� � �������, �� ����� ��� ��� ����� ��� �����.
� ������ ������� ������� ������� False.
��������� ������� ����� �� �������� �������.
������ �������� �� ���� ��������� �������� ������� ���� �� ���������� �� �������� �����, � ����������� ����� ����.
'''
# ��� ��� ���

def is_there_consecutive(values_list):
	for i in range(len(values_list) - 1):
		if values_list[i] == values_list[i+1]:
			return True
	return False
	
def is_there_consecutive(values_list):
	r = any(a == b for a,b in zip(values_list[:-1], values_list[1:]))
	return r
	
r = is_there_consecutive([1,2,2,3,3,4])
r = is_there_consecutive('11')
r = is_there_consecutive('11')
print(r)