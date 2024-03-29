---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Текстові файли

Python підтримує багато різних типів файлів, але умовно їх можна розділити на два види: текстові та бінарні.
Текстові файли — це, наприклад, файли з розширенням `csv, txt, html, py` тобто будь-які файли, в яких інформація міститься у текстовому вигляді.
Бінарні файли — це зображення, аудіо та відео та інше подібне.
В залежності від типу файла взаємодія з ним може трішки відрізнятись.
Ми розглянемо роботу з текстовими файлами.

При роботі з файлами необхідно дотримуватись певної послідовності операцій:

1. відкрити файл.
1. прочитати з нього дані або ж записати дані у файл.
1. закрити файл.

## open()

Щоб почати роботу з файлом, його треба відкрити за допомогою функції open():

    :::python
	open(file, mode)
	
Перший параметр — це шлях до файлу у файловій системі.
Шлях до файлу може бути абсолютним, або ж відносним щодо запущеної програми на Python.

Другий параметр "mode" визначає у якому режимі ми хочемо відкрити файл. Існує 4 режими:

- r (Read). Файл відкривається для читання. Якщо файлу не існує, "піднімається" вийняток FileNotFoundError
- w (Write). Файл відкривається для запису. Якщо файлу не існує, його буде створено. 
Якщо файл вже існує, тоді усі дані які містяться у ньому будуть знищені.
- a (Append). Файл відкривається для дозапису.
Якщо файла не існує, його буде створено. 
Якщо файл вже існує, то усі дані будуть записані після вже існуючих.
- b (Binary). Файл відкривається у бінарному режимі. 
Застосовується з іншими режимами (w чи r).

Функції *open()* можна вказати у якому кодуванні файл, з яким ми хочемо працювати. Зробити це можна наступним чином: після вказання імені файла і режиму у якому він відкривається ми вказуємо ще один аргумент. Запусується це так:

> encoding=<кодування>

*<кодування>* — це об'єкт типу *str*, у якому у символьному вигляді представлена назва кодування тексту. Дуже зручно!

Наприклад, якщо ми хочемо читати з текстового файла який був записаний у кодуванні utf-8, то відкривати ми цей файл будемо наступним чином:

    :::python
    text_file = open('btc_rates.csv', 'r', encoding='UTF-8')

open() повертає нам об'єкт спеціального типу "файл".
Надалі з файлом взаємодіють через методи цього об'єкту.


## close()

Метод close() закриває файл. 
Після цього ми вже не маємо змоги робити щось з файлом.

Після закриття файлу звільняються усі ресурси операційної системи, які були виділені для відкриття файлу.

	:::python
	text_file = open('btc_rates.csv', 'r', encoding='UTF-8')
	# тут робота з файлом
	text_file.close()

## flush()

Усі операції по зчитуванню даних з файлу чи запису у нього певної інформації
виконує операційна система.
Як правило при кожній операції з файлом 
ОС не взаємодіє з фізичним носієм на якому розташовано файл.
Дані записуються чи зчитуються певними порціями 
і знаходяться в оперативній пам'яті.

Коли, наприклад, записуємо у файл 2 байти,
вони не опиняються одразу ж на фізичному носії,
а попадають у спеціальний буфер, тобто розміщуються в оперативній пам'яті.
Щоб дані фізично записались, треба виконати певні дії.

Метод flush() якраз і виконує цю функцію, 
тобто усі дані які знаходяться у буфері
і призначені для запису,
попадають на фізичний носій.

Те ж саме відбувається коли ми викликаємо метод close().

	:::python
	text_file = open('btc_rates.csv', 'r', encoding='UTF-8')
	# тут щось записуємо у файл, можливо (частина) буде лише у буфері
	text_file.flush() # буде гарантовано записано на носій
	# тут щось записуємо у файл, можливо буде лише у буфері
	text_file.close() # буде гарантовано записано на носій