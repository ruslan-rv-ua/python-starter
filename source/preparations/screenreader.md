---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Скрінрідер

Якщо Ви для роботи на комп'ютері використовуєте програми екраного доступу — для проходженння данного курсу рекомендується NVDA. 

Рекомендовані налаштування скрінрідера такі:

- для редактора Notepad++ включити проговорювання номерів рядків
- для редактора Notepad++ включити проговорювання або індикацію відступів у тексті
- для редактора Notepad++ включити максимальний рівень символів
- для консолі Windows включити максимальний рівень проговорювання символів
- для консолі Windows включити повідомлення при зміні динамічного контенту

## Крок за кроком: налаштування NVDA

Непоганою практикою при користуванні скрінрідером NVDA є створення профілів налаштувань для окремих програм. При перемиканні між програмами NVDA підключає відповідний профіль у якому можуть бути збережні зовсім різні налаштування.

Створимо профіль NVDA для роботи з текстовим редактором Notepad++

- Впевніться, що у вас відкритий редактор Notepad++ і його вікно активне
- У меню NVDA вибрати "Конфігураційні профілі"
- У відкрившомуся діалозі натиснути кнопку "Новий"
- У відкрившомуся діалозі активувати радіокнопку "Поточний додаток (notepad++)" і натиснути кнопку "Гаразд"
- Натиснути кнопку "Закрити"
- Знову відкривши діалог "Конфігураційні профілі" впевніться що створений Вами профіль активний
- У меню NVDA вибрати "Форматування документа"
- Позначити прапорець "Номери рядків"
- У комбінованому списку "Промовляти заглиблення рядку" обрати "Мовлення та звукові сигнали"
- Натиснути кнопку "Гаразд"
- Натискаючи комбінацію клавіш **NVDA + P** встановити рівень проговорення символів "Усі"

У подальшому Ви можети змінити налаштування для профілю впевнившись попередньо що він активний.

Подібним способом створити профілі і зробити бажані налаштування для консолі Windows, інтернет-браузера.

## Перегляд тексту консолі Windows за допомогою NVDA.

NVDA дозволяє читати вміст екрану, поточного документа чи поточного об'єкта посимвольно, по словах або по рядках. Ця функція в основному корисна в консольних вікнах Windows, або у тих місцях, де можливості системної каретки обмежені, або вона взагалі відсутня. Наприклад, ви можете використовувати цю функцію для читання довгих інформаційних повідомлень у діалогових вікнах. 

 При переміщенні переглядового курсора, системна каретка не рухається, що дозволяє вам безперешкодно читати текстове наповнення об'єкта, не втрачаючи при цьому позицію редагування тексту. Проте, типово, при переміщенні системної каретки переглядовий курсор рухається слідом за нею. Цю фунцію можна вмикати та вимикати. 
 
 Для перегляду тексту доступні такі клавіші:
 
 
|Ім'я|Desktop-розкладка|Laptop-розкладка|Опис|
|-|-|-|-|
|Переміститися на верхній рядок перегляду|шіфт+додаткова7|NVDA+контрол+на початок|Переміщає курсор на верхній рядок поточного об'єкта|
|Перейти до попереднього рядка перегляду|додаткова7|NVDA+стрілка вгору|Переміщає курсор до попереднього рядка у поточному об'єкті|
|Повідомити поточний рядок перегляду|додаткова8|NVDA+шіфт+.|Читає поточний рядок об'єкта. Натисніть двічи для посимвольного читання, натисніть тричі для читання фонетичного опису символів.|
|Перейти до наступного рядка перегляду|додаткова9|NVDA+стрілка вниз|Переміщає переглядовий курсор до наступного рядка текстового перегляду|
|Перейти до найнижчого рядка перегляду|шіфт+додаткова9|NVDA+контрол+в кінець|Переміщає переглядовий курсор до останнього рядка текстового перегляду|
|Перейти до попереднього слова перегляду|додаткова4|NVDA+контрол+стрілка вліво|Переміщає переглядовий курсор на попереднє слово в тексті поточного об'єкта|
|Повідомити поточне слово|додаткова5|NVDA+контрол+.|Повідомляє слово, на якому знаходиться переглядовий курсор. Натисніть двічі для посимвольного читання, натисніть тричі для читання фонетичного опису символів.|
|Перейти до наступного слова перегляду|додаткова6|NVDA+контрол+стрілка вправо|Переміщує переглядовий курсор на наступне слово в тексті поточного об'єкта|
|Переміститись на початок рядка|шіфт+додаткова1|NVDA+на початок|Переміщає переглядовий курсор на початок поточного рядка перегляду|
|Переміститись на початок рядка|шіфт+додаткова1|NVDA+на початок|Переміщає переглядовий курсор на початок поточного рядка перегляду|
|Переміститись на попередній символ|додаткова1|NVDA+стрілка вліво|Пролистати вліво (текстовий режим) 	Переміщає переглядовий курсор на попередній символ у поточному рядку перегляду|
|Повідомити поточний символ перегляду|додаткова2|NVDA+.|Повідомляє символ у поточному рядку, на якому знаходиться переглядовий курсор. Натисніть двічи для фонетичного опису символа або прикладу, що починається із цього символа. Натисніть тричі для отримання ASCII та шіснадцятизначного значення символа.|
|Переміститись на наступний символ перегляду|додаткова3|NVDA+стрілка вправо|Переміщає переглядовий курсор на наступний символ у поточному рядку|
|Переміститися в кінець поточного рядка перегляду|шіфт+додаткова3|NVDA+в кінець|Переміщає переглядовий курсор у кінець поточного рядка перегляду|
|Читати все від переглядового курсора|додатковий Плюс|NVDA+шіфт+a|Читає від поточної позиції курсора, і переміщує його за текстом|
|Копіювати від переглядового курсора|NVDA+f9|NVDA+f9|Помічає поточну позицію переглядового курсора в тексті як початкову для виділення чи копіювання. Копіювання не буде виконано доти, поки ви не вкажете NVDA кінцеву позицію, до якої копіювати|
|Копіювати до переглядового курсора|NVDA+f10|NVDA+f10|Одноразове натискання виділяє весь текст від попередньо встановленої початкової помітки до позиції переглядового курсора; подвійне натискання копіює текст в буфер обміну. Після натискання цієї комбінації клавіш текст потрапить до буфера обміну Windows.|
|Повідомити форматування тексту|NVDA+f|NVDA+f|Повідомляє форматування тексту в місці розташування переглядового курсора|

Увага! Для того, щоб клавіші цифрового блоку (numpad) правильно виконували свої функції, режим Numlock повинен бути вимкненим. 


## Завдання
- Впевніться що налаштування Вашого скрінрідера дозволяють детально читати тексти програм на Python у текстовому редакторі і цьому документі.
- Впевніться що налаштування Вашого скрінрідера дозволяють детально читати вміст консолі Windows
