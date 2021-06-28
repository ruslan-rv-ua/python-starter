---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Методи

Над об'єктами можна виконувати певні дії, 
і ці дії здебільшого залежать якого характеру дані містяться в об'єкті, 
або ж, як ми вже з'ясували, до якого типу відноситься об'єкт.
Над числами ми можемо виконувати одні дії, над символьними рядками інші, над списками — ще інші.

Дії над об'єктами зручно виконувати за допомогою функцій передаючи їм об'єкти як аргумент.
Але оскільки над об'єктами різних типів виконуються різні дії, 
то може виникнути ідея:
як би зробити так, щоб у об'єктів певного типу були тільки свої функції?

Якщо ідея непогана, то треба її реалізовувати!
І в Python ми зустрічаємо таке нове поняття, як "методи".

Метод — це по суті функція, яка "закріплена" за певним об'єктом і яка виконує певні дії над цим об'єктом.

Записується це наступним чином: об'єкт чи посилання на нього, далі ставиться крапка, і після крапки метод об'єкта:

	object.method()
	
У наведеному вище прикладі "object" — це об'єкт,
а "method" — його метод.
Пам'ятаючи що метод — це функція, його можна викликати, що й означають круглі дужки після імені метода.

Ми поки що не знаємо жодного метода для жодного типу даних,
але давайте розглянемо на прикладах як в Python виглядає виклик методів.

	l = [1, 2, 3]  # змінна "l" вказує на список
	l.pop()  # викликаємо метод pop об'єкту який належить до типу list
	l.pop(0)  # метод — це функція, отже їй можна передавати аргументи
	[1,2,3].pop()  # викликаємо метод pop об'єкту типу list, об'єкт вказано явно
		
	s = 'Happy New Year' # s — це символьний рядок
	s.split()  # викликаємо метод split об'єкту типу str
	'a b c'.split(' ')  # викликаємо метод split об'єкту типу str з одним аргументом типу str