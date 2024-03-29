---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Форматування символьних рядків

Припустимо маємо дві змінні:

	:::python
	>>> name = 'Даринка'
	>>> age = 25
	
Використовуючи значення цих змінних нам треба сформувати наступний текст:

> Мене звати Даринка і мені 25 років.

Скористаємось конкатенацією. Не забуваємо приводити числа до `str`:

	:::python
	>>> s = 'Мене звати ' + name + ' і мені ' + str(age) + ' років.'
	>>> s
	'Мене звати Даринка і мені 25 років.'
	>>>
	
Що ми зробили? Використовуючи дані сформували певним чином символьний рядок. 
Так само можна сформувати інший рядок використавши інші дані. 
Говорять, що ми "відформатували дані у символьному рядкові". 
Спосіб зрозуміли, але трохи громіздкий. 
В Python для формування символьних рядків є більш зручний механізм — 
"форматовані рядки", або "f-рядки" (f-strings). 

Суть у тому, що використовуючи літерал символьного рядка ми одразу ж вказуємо дані, 
які треба підставити у цей символьний рядок. 

Для вказівки, що рядок не простий, а форматований, перед літералом ставлять букву "f":

	:::python
	s = f'Це форматований рядок'
	
Дані, які треба включити в рядок, 
вказують у фігурних дужках:

	:::python
	>>> name = 'Даринка'
	>>> age = 25
	>>> s = f'Мене звати {name} і мені {age} років.'
	>>> s
	'Мене звати Даринка і мені 25 років.'
	>>>

Такий спосіб форматування рядків набагато читабельніший, зрозуміліший. 

Використовувати можна лише вже існуючі у програмі дані:

	:::python
	>>> f'{unknown_variable}'
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'unknown_variable' is not defined
	>>>
	
Можна використовувати навіть вирази:

	:::python
	>>> a = 2
	>>> b = 3
	>>> f'{a}+{b}={a+b}'
	'2+3=5'
	>>>

Часто, коли треба діяти швидко, при зневадженні програм виводять значення змінних за допомогою `print()`. 
Виглядає це приблизно так:

	:::python
	print('total=', total)
	
Використовуючи f-strings робити це можна простіше:

	:::python
	print(f'{total=}')
