---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# elif
		
Логіка виконуваної програми може бути складніша, 
ніж вибір однієї з двох гілок. 
Наприклад, залежно від значення тієї чи іншої змінної, 
може виконуватися одна з трьох (або більше) гілок програми. 

Як організувати таке множинне розгалуження? 
Напевно, можна використовувати декілька інструкцій if: 
спочатку перевіряється умовний вираз у першій інструкції if 
(якщо він True, 
то буде виконуватися вкладений в неї блок коду), 
потім у другій інструкції if і т.д. 

	:::python
	if x > 0:
		print(1)
	if x < 0:
		print(-1)
	if x == 0:
		print(0)

Однак при такому підході перевірка наступних інструкцій буде продовжуватися навіть тоді, 
коли перша умова була True, 
і блок коду при даній гілці був виконаний. 
Перевірка наступних умов може виявитися безглуздою.

Можна побудувати логіку вибору за допомогою вкладених `if`:

	:::python
	if x > 0:
		print(1)
	else:
		if x < 0:
			print(-1)
		else:
			print(0)

Але такий код читається і сприймається вже складніше. 
А тут лише один рівень вкладеності `if`. 
А якщо варіантів вибору буде, припустимо, 5, 
наскільки легко буде сприймати такий код? 
Здається, що не дуже... 
Перший варіант був сприймався набагато краще, хоча виявився неефективним. 

В Python передбачено спеціальне розширення інструкції if, 
що дозволяє направити потік виконання програми з одній гілок. 
Дана розширена інструкція, 
крім необов'язкової частини else, 
містить ряд гілок elif 
(скорочення від "else if" - "інакше якщо").
Частин elif може бути як завгодно багато (в межах розумного, звичайно).

Приклад:

	:::python
	if x > 0:
		print(1)
	elif x < 0:
		print(-1)
	else:
		print(0)

Зауважте: інструкція `else` може бути відсутня. 
