'''
Напишіть програму яка виконує наступне:
1. Присвоїти змінній text наступне значення: 'I amy Jane.'
2. Змінній n присвоїти наступне значення: 5
3. Видалити з символьного рядка text символ з порядковим номером n. Результат присвоїти змінній text
4. Вивести значення змінної text
'''
# ваш код починається тут
text = 'I amy Jane.'
n = 5
text = text[:n-1] + text[n:]
print(text)

# не міняйте наступний код
assert text == 'I am Jane.'