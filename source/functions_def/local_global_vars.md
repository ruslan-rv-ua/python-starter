Всередині функції можна використовувати змінні,
які були оголошені поза цією функцією:

	:::python
	def f():
		print(var)
	var = 'присвоєно поза функцією'
	f()
	
Результат:

	присвоєно поза функцією
	
Тут змінній "var" присвоюється значення "1", 
і функція "f" виводить це значення, не дивлячись на те, 
що вище функції f ця змінна не ініціалізується. 
Але у момент виклику функції "f№ змінній "var" 
вже присвоєно значення, 
тому функція "f" може вивести його.

Такі змінні (які оголошені поза функцією, 
але доступні всередині функції) 
називають *глобальними*.

Але якщо ініціалізувати якусь змінну 
всередині функції, 
використовувати цю змінну 
поза функцією вже не вдасться. 
Приклад:

	:::python
	def f():
		var = 'присвоєно всередині функції'
	f()
	print(var)

Отримаємо вийняткову ситуацію

	NameError: name 'var' is not defined
	
що означає: "ім'я 'var' не визначене".

Змінні, які оголошені всередині функції, 
називають *локальними*. 
Ці змінні стають недоступными після виходу з функції.

А що буде, якщо спробувати змінити значення 
глобальної змінної всередині функції?

	:::python
	def f():
		var = 'присвоєно всередині функції'
		print(var)
	var = 'присвоєно поза функцією'
	f()
	print(var)

Отримаємо наступний результат:

	присвоєно всередині функції
	присвоєно поза функцією
 
Тобто не дивлячись на те, 
що значення змінної "var" змінилось всередині функції, 
поза функцією воно залишилось незмінним! 
Що не так?

Якщо всередині функції модифікується значення деякої змінної,
то змінна з таким ім'ям вважається локальною,
і її модифікація не призведе до зміни глобальної змінної
з таким самим ім'ям.

Більш формально: 
якщо всередині функції 
є хоча б одна інструкція, 
яка модифікує значення змінної
то така змінна вважається локальною
і не може бути використана до ініціалізації.

Модифікувати змінну можна або ж оператором присвоєння,
або ж використавши її у циклі `for` (про цикли дізнаємось пізніше).

Зауважте, що навіть якщо модифікація змінної
ніколи не відбудеться за логікою коду,
інтерпретатор про це ніяк не може здогадатися,
і се одно буде вважати змінну як локальною.  
Приклад:

	:::python
	def f():
		print(var)
		if False:
			var = 'присвоєно всередині функції'
	f()

Отримаємо вийняток: 

	UnboundLocalError: local variable 'var' referenced before assignment

Що означає: "використання локальної змінної 'var' перед присвоєнням їй значення".
В функції "f" 
змінна "var" стає локальною тому
що у функції є команда 
яка модифікує її,
навіть якщо вона ніколи і не буде виконана.
