В Python типи даних ще називають *класами*.

	s = 'string'
	
Можна сказати що змінна *s* типу "символьний рядок", або належить до класу *str*.

-----
## Якого ти типу?

В Python є функція *type()*, яка дозволяє нам визначити до якого класу належить її аргумент, або ж іншими словами якого типу є переданий ій аргумент.

	>>> type(1)
	<class 'int'>
	>>> type(1.1)
	<class 'float'>
	>>> type('Hello')
	<class 'str'>
	>>>

-----
## Хочу в інший клас!

Деколи виникає необхідність перетворити один тип даних в інший.  
Розглянемо приклад:

	>>> a = '123'
	>>> b = '321'
	>>> type(a)
	<class 'str'>
	>>> type(b)
	<class 'str'>
	>>>

Змінні *a* і *b* рядкового типу, хоча усі символи які містяться в них є цифрами і разом усі символи у кожній змінній представляють ціле число.
Припустимо ми хочемо отримати суму цих чисел.
Додавання — це арифметична операція.
Ми не можемо виконувати арифметичні операції над рядками.
Було б непогано зробити так, щоб те, що міститься у рядках перетворились на цілі числа,
тоді ми легко виконаємо додавання над цілими числами.

Щоб перетворити щось певного типу у тип цілого числа в Python є функція int:

	>>> num = int('100500')
	>>> type(num)
	<class 'int'>
	>>>

Коли ми бачимо запис типу

	int(arg)
	
ми говоримо що *привели arg до типу int*.

Розвиваючи приклад з двома змінними рядкового типу:

	>>> a = '123'
	>>> b = '321'
	>>> x = int(a)
	>>> x
	123
	>>> type(x)
	<class 'int'>
	>>> y = int(b)
	>>> y
	321
	>>> x + y
	444
	>>> int(a) + int(b)
	444
	>>>

В Python є функції для приведення до інших типів, розглянемо деякі з них:

|Функція|Опис|
|-|-|
|int(arg)|перетвоює arg у ціле число|
|float(arg)|перетвоює arg у дробове число|
|str(arg)|перетвоює arg у символьний рядок|
<!---
|tuple(arg)|перетвоює arg у кортеж|
|list(arg)|перетвоює arg у список|
|dict(arg)|перетвоює arg у словник|
-->

Розглянемо приклади приведення до різних типів даних

-----
#### int()

	>>> int('777')
	777
	>>> int(23.2)
	23
	>>> int('23.2')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '23.2'
	>>> int()
	0
	>>>


-----
#### float()

	>>> float(2)
	2.0
	>>> float('2')
	2.0
	>>> float('2.2')
	2.2
	>>> float()
	0.0
	>>>

-----
#### str()

	>>> str(1)
	'1'
	>>> str(1.1)
	'1.1'
	>>> str()
	''
	>>>

<!--
-----
#### tuple()

	>>> tuple( [1, 2, 3] )
	(1, 2, 3)
	>>> tuple( 'Python' )
	('P', 'y', 't', 'h', 'o', 'n')
	>>> tuple( 1 )
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'int' object is not iterable
	>>> tuple()
	()
	>>>



-----
#### list()

	>>> list( (1, 2, 3) )
	[1, 2, 3]
	>>> list( "It's cool!" )
	['I', 't', "'", 's', ' ', 'c', 'o', 'o', 'l', '!']
	>>> list(1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'int' object is not iterable
	>>> list()
	[]
	>>>


-----
#### dict()

	>>> dict( [ (1, 2), (3, 4) ] )
	{1: 2, 3: 4}
	>>> dict()
	{}
	>>>
-->