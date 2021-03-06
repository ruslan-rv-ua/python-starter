---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Визначення функцій

Визначення (створення) функції складається із заголовка і тіла функції.
Першим рядком іде заголовок:
спочатку вказується інструкція "def",
потім обране ім'я функції, 
за яким слідує пара круглих дужок, 
в яких можна вказати імена деяких змінних (параметри функції), 
і двокрапка у самому кінці. 
Далі йде тіло функції — блок команд з відступом.

Розглянемо простий приклад:

	:::python
	def say_hello():
		print('Hello, World!')
		
Ми визначили функцію з іменем "`say_hello`".

Сама функція виконуються лише тоді, 
коли вона викликається в основній гілці програми.

Виконуються усі інструкції, які входять у тіло функції. 

Закінчимо попередній приклад і напишемо код
який оголошує функцію і викликає її двічі:

	:::python
	def say_hello():
		print('Hello, World!')
	say_hello()
	say_hello()
	
Якщо запустити вищенаведений код на виконання,
то отримаємо наступне:

	Hello, World!
	Hello, World!
	>>>

Зауважте, що
якщо функція присутня у вихідному коді, 
але ніде не викликається в ньому, 
то вона не буде виконуватись в програмі жодного разу. 

Оскільки інтерпретатор Python виконує програму послідовно рядок за рядком, 
визначення функції має бути розташовано вище ніж її виклик. 
Спроба викликати ще не оголошену функцію призведе до помилки:

	:::python
	say_hello()
	def say_hello():
		print('Hello, World!')

При спробі виконати такий код отримаємо:

	NameError: name 'say_hello' is not defined

