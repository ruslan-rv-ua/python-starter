# Мутабельні і немутабельні об'єкти

У списку можна поміняти елемент знаючи його індекс:

	:::python
	>>> l = [1,2,3]
	>>> l[0] = 7
	>>> l
	[7, 2, 3]
	>>>
	
Символьні рядки теж можна індексувати. 
А чи можна у символьному рядку поміняти символ?

	:::python
	>>> s = 'Саша'
	>>> s[0] = 'П'
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment
	>>>
	
Отримали помилку:

>Об'єкти типу 'str' не підтримують присвоєння елементам

У кортежі також неможливо поміняти елемент, нам вже про це відомо. 
Виходить що у списках поміняти елемент можна, а у символьному рядку і кортежі — ні. 
Чому так?

Об'єкти в Python поділяються на два типи:

- значення (стан) яких можна змінити після їх створення, будемо називати їх *мутабельними* (від англ. *mutable*)
- значення яких змінити неможливо, будемо називати їх *немутабельними* (*immutable*)

Об'єкти одних типів даних є мутабельними, об'єкти інших — немутабельними. 
Тому можна говорити про мутабельні і немутабельні типи даних. 
До мутабельних типів даних з вже знайомих нам відноситься `list`, 
до немутабельних — `int, float, str, bool, tuple`.

Якщо нам необхідно отримати нове значення змінивши дані немутабельного типу, 
ми просто створюємо новий об'єкт:

	:::python
	>>> s = 'Саша'
	>>> id(s)
	2567709384496
	>>> s = 'П' + s[1:]
	>>> s
	'Паша'
	>>> id(s)
	2567716119920
	>>>

Дані об'єктів мутабельних типів ми можемо модифікувати прямо у вже існуючому об'єкті:

	>>> a = [1,2,3]
	>>> b = a # a і b посилаються на один список [1,2,3]
	>>> a == b # рівні по значенню
	True
	>>> a is b # вказують на один об'єкт
	True
	>>> b[0] = 777 # змінюємо список на який посилаються a і b
	>>> a
	[777, 2, 3]
	>>> b
	[777, 2, 3]
	>>>

А як же бути, якщо ми хочемо створити новий мутабельний об'єкт, але дані взяти з іншого? 
У такому разі при створенні нового мутабельного об'єкта нам необхідно 
зкопіювати дані з іншого. 
Зрізання завжди створює і повертає новий об'єкт. 
Скористаємось цим:

	:::python
	>>> a = [1, 2, 3]
	>>> b = a[:]
	>>> a == b # рівні значення
	True
	>>> a is b # різні об'єкти
	False
	>>> a[0] = 777
	>>> a
	[777, 2, 3]
	>>> b
	[1, 2, 3]
	>>>
