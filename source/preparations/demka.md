---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---
# Засіб перегляду демонстраційного коду

В процесі навчання для зручної демонстрації програмного коду користувачам 
які користуються скрінрідером автором даного курса було розроблено спеціальний засіб. 
Принцип його роботи наступний:

- Ви запускаєте програму на Python.
- Програма періодично підвантажує текстовий файл з віддаленого сервера і якщо він змінився, то зберігає його на Вашому локальному комп'ютері.
- Ви відкриваєте завантажений файл у текстовому редакторі і можете вивчати і запускати на виконання програмний код.
- Коли файл на Вашому локальному комп'ютері оновлюється лунає звуковий сигнал.
- Почувши звукову індикацію що свідчить про оновлення файлу Вам необхідно перезавантажити його у текстовому редакторі.


##### Крок за кроком: підготовка засобу перегляду демонстраційного коду
1. Завантажте наступний файл:  
[demka.zip](demka.zip)
1. У корені диску "C:" створіть теку з наступною назвою:  
>dev
1. Розпакуйте завантажений архів у створену теку. 
1. У теці `C:\dev\demka` знайдіть файл `demka.exe`. Це є файл запуска програми.
1. У теці `C:\dev\demka\editor` знайдіть файл `notepad++.exe`. Це є файл запуска текстового редактора Notepad++
