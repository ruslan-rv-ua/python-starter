---
hide:
#  - navigation # Hide navigation
#  - toc        # Hide table of contents
---

# Прийоми використання циклів

Цикли використовують для багатьох класів задач. 
Розглянемо зараз деякі з них. 

## Агрегація даних

Окремий клас задач, який не може обійтись без циклів, 
має назву ***"агрегування даних"***. 
До таких задач відносяться, наприклад, 
пошук максимального або мінімального значення серед певного набору даних, 
суми або середнього арифметичного набору чисел і таке інше. 
Їх головна особливість полягає у тому, 
що результат залежить від усього набору даних. 
Наприклад щоб обчислити суму необхідно скласти усі числа з набору, 
а щоб знайти максимальне потрібно порівняти усі числа. 

Розглянемо приклад: 
необхідно створити функцію, яка буде знаходити суму чисел у вказаному діапазоні. 

Для реалізації такого кода нам знадобиться цикл, 
оскільки додавання чисел — це ітеративний процес, 
тобто він повторюється для кожного числа, 
а кількість ітерацій залежить від розміру діапазона.

	:::python
	def sum_of_range(from_inclusive, to_exclusive):
		sum = 0
		number = from_inclusive
		while number < to_exclusive:
			sum += number
			number += 1
		return sum

У задачах на агрегацію завжди є якась змінна, 
у якій зберігається результат роботи цикла. 
У нашому прикладі це змінна `sum`. 
При кожній ітерації цикла відбувається її модифікація: 
додавання чергового числа з діапазона. 

Змінній `sum` задається початкове значення, а саме 0. 
Будь-яка операція, що повторюється, починається з якогось значення. 
В математиці є таке понятие нейтральний елемент операції.  
Це означає, що операція з цим елементом не змінює те значення, над яким відбувається операція. 
При додаванні будь-якого числа і 0 отримаємо саме число, 
при відніманні — так само. 

У кожної операції свій нейтральний елемент. 
Спробуйте визначити який нейтральний елемент у операції множення. 

Агрегацію можна застосовувати не лише для чисел. 
Давайте реалізуємо свою власну мультиплікацію символьних рядків. 
Будемо використовувати конкатенацію, 
нейтральний елемент для останньої — пустий символьний рядок.

	:::python
	def multiply_string(string, times):
		result = ''
		while times > 0:
			result += string
			times -= 1
		return result

## Обхід символьних рядків

До окремого символа рядка можна дістатись знаючи його індекс. 
Для будь-якого символьного рядка індексом першого символа буде 0, 
а для останнього — довжина рядка мінус 1. 

Створимо функцію, яка виводить усі символи з рядка:

	:::python
	def print_symbols(string):
		i = 0
		while i < len(string):
			print(string[i])
			i += 1
	print_symbols('Hello')
	
Результат:

	:::python
	H
	e
	l
	l
	o
	>>>

При проході символьних рядків змінній, яка відповідає індексу, 
часто дають назву "i" від англійського "index". 





