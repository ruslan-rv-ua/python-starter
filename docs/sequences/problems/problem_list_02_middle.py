'''
"Дай середній!"

Припустимо називати середнім елементом списку такий елемент, 
який має рівні порядкові номери якщо рахувати з початку і з кінця списка. 
Наприклад для списка
['start', True, 5]  
середнім елементом буде True.
Створіть функцію get_middle(), яка приймає список.
Якщо у переданому списку непарна кількість елементів,
то фунція повертає середнії елемент цього списка.
Інакше функція повертає None
'''

def get_middle(l):
	# ваш код починається тут

# не міняйте наступний код
assert get_middle([]) is None
assert get_middle([1]) == 1
assert get_middle([1, 1]) is None
assert get_middle([1, 2, 3]) == 2
assert get_middle([1, 2, 3, 4, 5]) == 3
assert get_middle(list(range(100))) is None