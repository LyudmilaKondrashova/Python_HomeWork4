#1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from cmath import pi

d = input('Введите заданную точность числа Пи в пределах от 10^{-10} до 10^{-1}:\n')
if 10**(-10) <= float(d) <= 10**(-1):
    print(str(pi)[:len(d)])
else:
    print('Введите точность в указанном диапазоне!')


#2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N
numbN = int(input('Введите натуральное число:\n'))
spis_mn = [1]
delit = 2
while delit*delit <= numbN:
    if numbN % delit == 0:
        spis_mn.append(delit)
        numbN //= delit
    else:
        delit += 1
if numbN > 1:
    spis_mn.append(numbN)
print(f'Список простых делителей числа: {spis_mn}')


#3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
count_spis = int(input('Введите количество элементов списка\n'))
print('Введите элементы списка через клавишу Enter')
spis =[]
spis_new = []
for i in range(count_spis):
    spis.append(int(input()))
for i in range(count_spis):
    fl = False
    for j in range(count_spis):
        if spis[i] == spis[j] and i != j:
            fl = True    
    if not fl:
        spis_new.append(spis[i])
print(f'Исходная последовательность: {spis}')
print(f'Список неповторяющихся элементов исходной последовательности: {spis_new}')


#4. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def polynomial(deg, f_name):
    import random
    str_polynomial = ''
    for i in range(deg+1):
        koeff = random.randint(0,100)
        if koeff > 1:
            if i < deg-1:
                str_polynomial += str(koeff) + '*x^' + str(deg-i) + '+'
            elif i == deg-1:
                str_polynomial += str(koeff) + '*x' + '+'
            else:
                str_polynomial += str(koeff)
        elif koeff == 1:
            if i < deg-1:
                str_polynomial += 'x^' + str(deg-i) + '+'
            elif i == deg-1:
                str_polynomial += 'x' + '+'
            else:
                str_polynomial += str(koeff)
    if str_polynomial[len(str_polynomial) - 1] == '+':
        str_polynomial = str_polynomial[:-1]
    str_polynomial = str_polynomial + ' = 0'
    file_polynomial = open(f_name,'w')
    file_polynomial.writelines(str_polynomial)
    file_polynomial = open(f_name,'r')
    print(file_polynomial.read())
    file_polynomial.close()
    

# step_k = int(input('Введите натуральную степень многочлена:\n'))
# if step_k > 0:
#     polynomial(step_k, 'file_polynomial.txt')
# else:
#     print('Введена не натуральная степень!')


#5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
deg1 = int(input('Введите натуральную степень 1-ого многочлена:\n'))
if deg1 > 0:
    deg2 = int(input('Введите натуральную степень 2-ого многочлена:\n'))
    if deg2 > 0:
        polynomial(deg1, 'file_polynomial1.txt')
        polynomial(deg2, 'file_polynomial2.txt')
    else:
        print('Введена не натуральная степень!')
else:
    print('Введена не натуральная степень!')
exit
file1 = open('file_polynomial1.txt', 'r')
file2 = open('file_polynomial2.txt', 'r')
spis1 = file1.readline().split("+")
spis2 = file2.readline().split("+")
spis1_koeff = {}
for i in spis1:
    subsp1 = i.split("*")
    if len(subsp1) == 2:
        subspsp1 = subsp1[1].split("^")
        if len(subspsp1) == 2:
            spis1_koeff[f'{subspsp1[1]}'] = subsp1[0]
        else:
            spis1_koeff['1'] = subsp1[0]
    else:
        spis1_koeff['0'] = subsp1[0][:-4]
print(spis1_koeff)
spis2_koeff = {}
for i in spis2:
    subsp2 = i.split("*")
    if len(subsp2) == 2:
        subspsp2 = subsp2[1].split("^")
        if len(subspsp2) == 2:
            spis2_koeff[f'{subspsp2[1]}'] = subsp2[0]
        else:
            spis2_koeff['1'] = subsp2[0]
    else:
        spis2_koeff['0'] = subsp2[0][:-4]
print(spis2_koeff)
if len(spis2_koeff) > len(spis1_koeff):
    spis1_koeff,spis2_koeff = spis2_koeff,spis1_koeff