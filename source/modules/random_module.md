---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модуль random

Замість епіфграфа: ***«Генерація випадкових чисел занадто важлива, щоб залишати її на волю випадка»*** —  Роберт Кав'ю

Модуль random дозволяє генерувати випадкові числа. 
Зауважте, що Python генерує випадкові числа на основі формули, так що вони не насправді випадкові, а, як кажуть, псевдовипадкові. Але цей спосіб отримання випадкових чисел зручний для більшості задач (крім онлайн-казино).

### random()

Повертає псевдовипадкове число у діапазоні [0.0, 1.0)

    :::python
    >>> from random import *
    >>> random()
    0.7211406063548313
    >>> random()
    0.9399199478241781
    >>>

<!--    
## seed(a=None, version=2)
Налаштовує генератор на нову послідовність використовуючи число `a` (якщо вказано) або показник системного годинника. 

    :::python
    >>> seed()
    >>> random()
    0.6615122531907053
    >>> seed()
    >>> random()
    0.9369031218767864
    >>>
-->

### randint(a, b)

Повертає ціле випадкове число N, a <= N <= b.

    :::python
    >>> randint(-10,10)
    -1
    >>>

### choice(seq)

Повертає випадковий елемент з непустої послідовності `seq`. 

    :::python
    >>> choice([1,2,3])
    3
    >>> choice('абабагаламага')
    'а'
    >>>

### shuffle(x)

Перемішує елементи послідовності `x`. 

    :::python
    >>> List = [1,2,3,4,5,6,7,8,9]
    >>> shuffle(List)
    >>> List
    [8, 4, 1, 9, 2, 7, 3, 5, 6]
    >>>

<!--    
### sample(population, k)

Повертає список довжиною `k` унікальних елементів з послідовності `population`.

    :::python
    >>> sample(range(100),10)
    [84, 17, 89, 59, 94, 82, 80, 10, 25, 56]
    >>>
-->
    
## Додаткові матеріали

* [Документація Python. Модуль random](https://docs.python.org/3/library/random.html#random.randint)
* [Вікіпедія: Генерація випадкових чисел](https://uk.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D1%96%D1%8F_%D0%B2%D0%B8%D0%BF%D0%B0%D0%B4%D0%BA%D0%BE%D0%B2%D0%B8%D1%85_%D1%87%D0%B8%D1%81%D0%B5%D0%BB)
* Для "просунутих": [Безопасность случайных чисел в Python](https://habr.com/company/pt/blog/156133/)