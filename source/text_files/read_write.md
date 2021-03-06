---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Запис і читання текстових файлів

## write()

write() приймає у якості аргумента символьний рядок,
який, власне, і записується у файл.

Розглянемо приклад:

	:::python
	f = open('myfile.txt', 'w')
	f.write('Hello!\n')
	f.write('and goodbye')
	f.close()

Спочатку ми відкрили файл з ім'ям "myfile.txt" у режимі запису.
Далі ми записуємо у файл два символьні рядки, і потім закриваємо файл. Усе просто.

Зауважте: ми явно розділяємо рядки тексту за допомогою символу '\n'.


## writelines()

Writelines() отримує в якості аргумента
послідовність символьних рядків (список, кортеж, ...)
і записує усі елементи послідовності у файл:

	:::python
	a = ['Hi','there!']
	f = open('myfile.txt', 'w')
	f.writelines(a)
	f.close()

Зауважте що хоча ми й записуємо у файл одразу декілька рядків,
символ нового рядка автоматично не додається.
Тобто якщо виконати вищенаведений код,
то у текстовому файлі ми отримаємо:

>Hithere!


## read()

Метод read() зчитує усі дані з текстового файла
і повертає їх як один символьний рядок.




## readline()

Зазвичай текстова інформація у файлі
розбивається на окремі рядки,
і, подьтесь, було б дуже зручно
отримувати дані з файлу якраз окремими рядками.

Метод `readline()` при кожному виклику
зчитує з файлу черговий рядок 
і повертає його як символьний рядок.
Вважається що окремі рядки тексту у файлі
розділяються символом '\n'
і його буде включено до результату
який повертає метод `readline()`.


## readlines()

А чи можна отримати вміст усього файлу
але окремими символьними рядками?
Ну якщо дуже хочеться, то звісно так.

Метод `readlines()` зчитує усі дані з файлу,
розділяє їх на окремі символьні рядки
і повертає список з цих рядків.

Зауважте що символ нового рядка '\n' також буде присутнім у кожному символьному рядку.


## Файл як послідовність

Якщо текст у файлі розбитий на окремі рядки, то його можна вважати за послідовність символьних рядків.

Напишемо програму яка зчитує з текстового файлу рядок за рядком і виводить їх:

	:::python
	file = open('readme.txt', 'r')
	for line in file:
		print(line)
	file.close()



