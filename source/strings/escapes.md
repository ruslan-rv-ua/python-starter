# Екрановані послідовності

Екрановані послідовності дозволяють включити у рядок символи, які важко ввести з клавіатури. 

Екранована послідовність виглядає так: символ бекслеш (зворотній слеш) і зразу за ним один або декілька символів. 
Ось деякі такі послідовності:

|Екранована послідовність|Призначення|
|-|-|
|`\n`|новий рядок|
|`\r`|початок рядка|
|`\t`|табуляція|
|`\a`|"Дзвінок"|
|`\'`|апостроф|
|`\"`|лапки|
|`\\` |бекслеш|

Коли ми вказуємо інтерпретатору ім'я рядкової змінної, то екрановані послідовності виводяться саме так, як ми їз вказали. 
Щоб "задіяти" екрановані послідовності треба скористатись *print*. Порівняйте:

	>>> s = 'рядок 1\nрядок 2'
	>>> s
	'рядок 1\nрядок 2'
	>>> print(s)
	рядок 1
	рядок 2
	>>>

У даному випадку послідовність *\n* "новий рядок" спрацювала коли ми вивели значення змінної за допомогою *print*.

Ще приклади:

	>>> s = '"It\'s cool!" - she said.'
	>>> s
	'"It\'s cool!" - she said.'
	>>> print(s)
	"It's cool!" - she said.
	>>>

Екранування можна відключити, для цього перед початковими лапками чи апострофом вказують символ *r*. Такі рядки називають *сирими*.

	>>> path = r'C:\new_folder'
	>>> print(path)
	C:\new_folder
	>>> path
	'C:\\new_folder'
	>>>
