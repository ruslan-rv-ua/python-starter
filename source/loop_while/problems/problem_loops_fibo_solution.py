'''
"Фібоначчі"

Послідовність Фібоначчі — послідовність чисел. 
Перші два числа послідовності — 1, 1.
Кожне наступне число послідовності отримуємо сумою двох попередніх.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Реалізуйте функцію fibo(n) яка повертає число Фібоначчі з порядковим номером n.
'''
def fibo(n):
	# ваш код
	if n < 3:
		return 1
	a = b = 1
	while n > 2:
		a, b = b, a + b
		n -= 1
	return b
	
def fibo(n):
	# ваш код
	a, b = 0, 1
	while n > 1:
		next = a + b
		a = b
		b = next
		# a, b = b, a + b
		n -= 1
	return b
	
assert fibo(1) == 1
assert fibo(2) == 1
assert fibo(3) == 2
assert fibo(4) == 3
assert fibo(5) == 5
assert fibo(6) == 8
assert fibo(7) == 13