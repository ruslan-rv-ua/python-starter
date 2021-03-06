---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модулі в Python

Модулем в Python називають
будь-який файл з програмою. 
Так! Усі ті програми, що писали Ви, 
можна назвати модулями. 

Усе те, що міститься в модулі, можливо використовувати в інших програмах. 
Наприклад функції, які містяться в модулі, або ж змінні яким присвоєні певні значення. 
Для цього спочатку модуль треба підключити, 
або кажуть що треба "імпортувати модуль". 

Можна імпортувати або увесь вміст модуля, або ж певні окремі його сутності. 

Однією з сторін популярності Python є те,
що на цій мові програмування вже написано
безліч різних модулів як кажуть "на усі випадки"
і які, звісно, можна (і треба!) використовувати у своїх програмах.

У комплекті разом з інтерпретатором 
містяться модулі для вирішення самих розповсюджених і повсякденних задач.
Далі розглянемо найбільш цікаві з них

- tkinter — кросплатформений графічний інтерфейс для програм.

- csv — модуль, який дозволяє працювати з файлами у форматі csv 
(Comma Separated Values) —
популярному форматі при імпорті і експорті даних 
з різноманітних таблиць
або баз даних.
Можна як читати, так і записувати дані у файли цього формату.

- email — обробка email повідомлень. 
Модуль не реалізує ніяких методів для відправки повідомлень
по протоколах SMTP або NNTP
(для цього використовують інші засоби), 
але містить функції для розбору структури email повідомлень,
перевірки списку пошти,
перетворення і багато іншого.

- smtplib — модуль для відправки повідомлень електроної пошти
по протоколу SMTP.

- gzip, zlib — модулі для роботи зі стиснутими даними. 
Дозволяє не тільки упаковувати/розпаковувати
файлові архіви популярних форматів zip, gzip, bz2, 
але й працювати з символьними рядками.

- http — модуль дозволяє працювати з інтернет ресурсами по протоколу HTTP,
відправляти запити GET/POST, 
отримувати відповіді на запити,
обробляти Cookie
і фактично реалізувати свій клієнт чи сервер.

- datetime — у модулі містяться методи для для отримання інформації,
перетворення, зміни дати і часу.
Можна перетворити дату у символьний рядок
або ж прочитати її з рядків різних форматів.
Також можна виконувати математичні операції
з датами і часом.

- os — взаємодія з операційною системою:
робота з файлами,
отримання інформації про інтерфейси ОС
і багато іншого.

- os.path — маніпуляції з шляхами файлової системи.

- sqlite — робота з реляційною базою даних SQLite.

- re — робота з регулярними виразами

- math — усе що стосується математики

- random — герератор випадкових чисел

- configparser — робота з конфігураційними файлами ".ini"
(часто використовується у Windows).

- json — робота з дуже популярним форматом передачі даних json: серіалізація, десеріалізація, файли.

- ssl — робота з відповідними сертифікатами

- xml — розбір, аналіз і робота з даними у форматі xml.

- collections — набір спеціальних типів даних — контейнерів,
які доповнюють стандартні вбудовані типи dict, list, set і tuple.

- threading — створення багатопотокових програм.
