'''
дано номер телефону у вигляді символьного рядка у форматі '(XXX) YYY-YY-YY',  
де XXX — код мобільного оператора України,  
YYY-YY-YY — власне номер абонента.  
Треба отримати даний номер телефону у міжнародному форматі: '+38XXXYYYYYYY'
'''

phone = '(097) 222-55-77'
parts = phone.split()
code = parts[0][1:-1]
number = ''.join( parts[1].split('-') )
int_phone = '+38' + code + number
print(phone, '=', int_phone)