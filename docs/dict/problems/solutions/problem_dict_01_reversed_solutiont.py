# ваш код з наступного рядка, умова задачі далі
def reversed_dict(d):
	result = {}
	for key, value in d.items():
		result[value] = key
	return result


'''
"Перевернути словник"

Реалізувати функцію reversed_dict() яка виконує наступне:
1. В параметрах отримує словник. Усі значення у словнику унікальні. Словник може бути пустим.
2. Повертає словник у якому ключі і значення з переданого словника поміняні місцями
Приклад:
Вхідні дані: {1:'One', 2:'Two', 3:'Three'}
Вихідні дані: {'One': 1, 'Two': 2, 'Three': 3}
'''
# не міняйте наступний код, це тести
assert reversed_dict({1:'One', 2:'Two', 3:'Three'}) == {'One': 1, 'Two': 2, 'Three': 3}
assert reversed_dict({None:None}) == {None:None}
assert reversed_dict({}) == {}