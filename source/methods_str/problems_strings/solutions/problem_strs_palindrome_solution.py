'''
"Паліндром"

Паліндром — слово, набір символів, словосполучення або віршований рядок, що однаково читається в обох напрямках (зліва направо та справа наліво).
Пробіли ігноруються. Регістр букв не має значення.
Реалізуйте функцію is_palindrome().
Функція отримує символьний рядок.
Повертає True якщо переданий рядок є паліндромом, False в іншому випадку.
'''
def is_palindrome(string):
	# ваш код тут
	string = string.lower().replace(' ', '')
	return string == string[::-1]

assert is_palindrome('Чи в окуня є Янукович') == True
assert is_palindrome('Три психи пили Пилипихи спирт') == True
assert is_palindrome('') == True
assert is_palindrome('12321') == True
assert is_palindrome('123421') == False