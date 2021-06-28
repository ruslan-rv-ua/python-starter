# Немутабельні винятки

Для деяких об'єктів немутабельних типів існують певні "тонкощі". 
Розглянемо їх. 

## Кешування об'єктів

Python кешує деякі значення немутабельних типів. 
Що це означає?

Деякі значення використовуються розробниками дуже часто, 
наприклад цілі числа 0 та 1. 
І з метою оптимізації швидкодії 
при кожному запуску 
інтерпретатор автоматично створює об'єкти з цими значеннями. 
У подальшому кожного разу, коли ми використовуємо такі значення, 
вже непотрібно створювати нові об'єкти. 
Будуть використовуватись вже існуючі. 

	:::python
	>>> a = 1
	>>> b = 1
	>>> a is b
	True
	>>>

Python кешує цілі числа від -5 до 256 включно. 

Кешуються ще деякі немутабельні значення:

	:::python
	>>> a = 'hello'
	>>> b = 'hello'
	>>> a is b
	True
	>>> a = 'hello world'
	>>> b = 'hello world'
	>>> a is b
	False
	>>>

Для об'єктів мутабельних типів гарантується що інтерпретатор завжди створює новий об'єкт. 
Тут не буде "сюрпризів" як з деякими значеннями немутабельних типів. 

<!--
Більш того, об'єкт з таким значенням протягом усієї сесії інтерпретатора 
буде існувати лише у одному екземплярі:
-->
	
Зауважте: усе сказане вище справедливо для реалізації інтерпретатора CPython. 
Для інших реалізацій інтерпретатора мови Python поведінка може бути іншою. 

## Унікальний None 
	
Тип `NoneType` має лише одне значення — `None`. 
І створюється лише один об'єкт зі значенням `None`. 
Ось тут такий крок зроблено "свідомо", не для оптимізації. 
Є навіть окрема назва для типів даних, 
для яких може бути створено 
лише один об'єкт: ***"сінглтон"***.
І якщо необхідно порівняти щось з `None`, замість

	if something == None:
	
можна (і треба) використовувати:

	if something is None:
