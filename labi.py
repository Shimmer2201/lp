"""
ЛАБА 4
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
"""
"""
LABA 6
precision_kalchugin = float(input("Введите  точность:"))
pi_kalchugin = 0
elem_kalchugin = 1
n_kalchugin = 1
while elem_kalchugin >= precision_kalchugin:#начало цикла while, который будет выполняться, пока elem_kalchugin больше или равен точности
    elem_kalchugin = 1 / (2*n_kalchugin - 1)#вычисляем текущее значение элемента ряда
    if n_kalchugin % 2 == 0:#проверка на четность
        pi_kalchugin-=elem_kalchugin#вычисление текущего элемента из pi_kalchugin если n_kalchugin четное
    else:
        pi_kalchugin+=elem_kalchugin#прибавляем текущий элемент к pi_kalchugin, если n_kalchugin нечетно
    n_kalchugin+=1#увеличиваем n_kalchugin на 1
pi_kalchugin = pi_kalchugin * 4
print("ПИ приближенно равно:", pi_kalchugin)#вывод приближенного значенние числа ПИ
print("Количество членов ряда:", n_kalchugin - 1)#вывод количества членов ряда, которое было необходимо вычислить для заданной точности

"""

"""
LABA 7
from tkinter import messagebox
x = int(input('Выберите варинат ввода: \n 1 - поэлементно \n 2 - в строчку \n'))
if x == 1:
    akalchugin = []
    for ikalchugin in range(10):
        x = input()
        akalchugin.append(x)
else:
    textkalchugin = input()
    akalchugin = textkalchugin.split(',')
text = ''
for i in range(len(akalchugin)):
    text += akalchugin[i] + '\n' 
messagebox.showinfo('список стран',text)
"""

"""
LABA 8
def akey(i):
    return 7*i[1] + 6*i[2] + 5*i[3]

countries = [['Австрия',3,5,2],['Германия',7,7,8],['Италия',2,6,2],['Канада',6,5,4]]
sort_countr = sorted(countries, key = akey, reverse=True)

print('Отсортированная таблица: ')

for i in sort_countr:
    print(i[0], i[1], i[2], i[3])
print('\nТаблица побед и очков: ')

for i in sort_countr:
    print(i[0], i[1]+i[2]+i[3], akey(i)) 
"""

"""
laba 4 individualka

vulnerabilities = {
    "VULN-20230321.2": "Microsoft Internet Control Message Protocol",
    "VULN-20230317.2": "Microsoft Remote Procedure Call Runtime",
    "VULN-20230317.1": "Microsoft Edge",
    "VULN-20230315.3": "Adobe Illustrator",
    "VULN-20230310.4": "Cisco IOS XR"
}

def get_company(vuln_code):
    match vuln_code:
        case "VULN-20230321.2":
            return "Microsoft"
        case "VULN-20230317.2":
            return "Microsoft"
        case "VULN-20230317.1":
            return "Microsoft"
        case "VULN-20230315.3":
            return "Adobe"
        case "VULN-20230310.4":
            return "Cisco"
        case _:
            return "Такой уязвимости не найдено"

vuln_code = input("Введите код уязвимости: ")
company = get_company(vuln_code)
print(f"Компания, выявившая уязвимость: {company}")
"""
"""
РЯД
import math
precision = float(input("Введите точность:"))
if precision <= 0 or precision >= 1: print("Точность должна быть положительной")
else:
    elem = 1
    sum = 0
    n = 1 
    while abs(elem)>=precision and n!=0:
        elem = math.sin(1/math.sqrt(n**(3/4)))
        sum+=elem
        n+=1
print("Сумма ряда:",sum)
print("Количество членов ряда:",n-1)
"""
