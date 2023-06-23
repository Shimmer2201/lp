print('Список стран: Россия, Англия, Австрия, Германия, Дания, Исландия, Италия, Нидерланды')
itemkalchugin = input('Введите название страны:')
coef = 0.5
match itemkalchugin.lower():
        case 'россия': coef = 0.4059
        case 'англия': coef = 0.4535
        case 'австрия': coef = 0.56
        case 'италия': coef = 0.3176
funtkalchugin = float(input('Введите количество фунтов:'))
result = funtkalchugin * coef
print('В стране', itemkalchugin, funtkalchugin, 'lb =', round(result, 2), 'kg')
