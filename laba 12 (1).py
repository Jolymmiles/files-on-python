from datetime import *

alphabet = {"А": "Андрей", "Б": "Борис", "В": "Валетин", "Г": "Галина", "Д": "Данил", "Е": "Евгений", "Ж": "Жанна",
            "З": "Захар", "И": "Иисус", "К": "Константин", "Л": "Лев", "М": "Марта", "Н": "Наталья", "О": "Олег",
            "П": "Прохор", "Р": "Рената", "С": "Снежана",
            "Т": "Тамир", "У": "Ульяна", "Ф": "Федор", "Ч": "Чарли", "Э": "Эльдар", "Ю": "Юлиан", "Я": "Яков",
            "а": "Андрей", "б": "Борис", "в": "Валетин", "г": "Галина", "д": "Данил", "Е": "Евгений", "Ж": "Жанна",
            "з": "Захар", "и": "Иисус", "к": "Константин", "л": "Лев", "м": "Марта", "н": "Наталья", "о": "Олег",
            "п": "Прохор", "р": "Рената", "с": "Снежана",
            "т": "Тамир", "у": "Ульяна", "ф": "Федор", "ч": "Чарли", "э": "Эльдар", "ю": "Юлиан", "я": "Яков", }
number_3 = {"0": "Ноль", "1": "Сто", "2": "Двести", "3": "Триста", "4": "Четыреста", "5": "Пятьсот",
            "6": "Шестьсот",
            "7": "Семьсот", "8": "Восемьсот", "9": "Девятьсот"}
number_2 = {"0": "Ноль", "1": "Десять", "2": "Двадцать", "3": "Тридцать", "4": "Сорок", "5": "Пятьдесят",
            "6": "Шестьдесят",
            "7": "Семьдесят", "8": "Восемьдесят", "9": "Девяносто"}
number_1 = {"0": "Ноль", "1": "Один", "2": "Два", "3": "Три", "4": "Четыре", "5": "Пять", "6": "Шесть",
            "7": "Семь", "8": "Восемь", "9": "Девять"}
digits = {"11": "Одинадцать", "12": "Двенадцать", "13": "Тринадцать", "14": "Четырнадцать", "15": "Пятнадцать",
          "16": "Шестнадцать",
          "17": "Семнадцать", "18": "Восемнадцать", "19": "Девятнадцать"}
while True:
    task = int(input('Введите номер задания: '))
    try:
        if task == 1:
            Flag = False
            file = open('enter.txt', mode='r')
            file_output = open('output.txt', mode='w')
            for line in file:
                if 'ФИО' in line:
                    continue
                line_split = line.split('|')

                output = f'Идентификация государственного регистрационного знака:{line_split[4]}30 регион \n'
                file_output.write(output)
                print(output)

                print('( ', end='')
                Flag = False
                numbers = line_split[4]
                code = '('
                number = numbers
                for i in range(len(number)):
                    # Буквы
                    if number[i] in alphabet:
                        print(alphabet[number[i]], end=' ')
                        code = code + alphabet[number[i]] + ' '

                    # Сотни
                    elif i == 2:
                        print(number_3[number[i]], end=' ')
                        code = code + number_3[number[i]] + ' '

                    # Десятки
                    elif i == 3 and 10 < (int(number[3] + number[4])) < 20:
                        print(digits[number[3] + number[4]], end=' ')
                        code = code + digits[number[3] + number[4]] + ' '
                        Flag = True
                    elif i == 3:
                        if number[2] == '0' and number[i] == '0':
                            print('Ноль', end=' ')
                            code = code + 'Ноль '
                        elif number[i] in '123456789':
                            print(number_2[number[i]], end=' ')
                            code = code + number_2[number[i]] + ' '

                    # Еденицы
                    elif i == 4:
                        if Flag == False:
                            if number[3] == '0' and number[2] == '0' and number[i] == '0':
                                print('Ноль', end=' ')
                                code = code + 'Ноль '
                            elif number[i] in '123456789':
                                print(number_1[number[i]], end=' ')
                                code = code + number_1[number[i]] + ' '

                code = code + '30 регион)\n'
                print('30 регион)', end='')
                file_output.write(code)
                print()

                output_last = f'Получатель: Банк России \n' \
                              f'Плательщик: {line_split[0]} \n' \
                              f'Адресс: {line_split[5]} \n' \
                              f'Постановление (УИН): 12354984654798 \n' \
                              f'Вид платежа: Штраф за нарушение ПДД \n' \
                              f'Дата: 20.04.2018 \n' \
                              f'Сумма:{line_split[9]}'
                print(output_last, end='')
                file_output.write(output_last)
                split_date = line_split[3].split('.')
                first_date = datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
                stage_driver = (datetime.now() - first_date).days
                stage_driver = stage_driver / 365
                stage_driver = str(stage_driver).split('.')
                task4 = f'Водительский стаж: {stage_driver[0]}\n'
                print(task4)
                file_output.write(task4)
                split_date_old = line_split[1].split('.')
                if int(split_date_old[0]) > 3:
                    split_date_old[0] = int(split_date_old[0]) - 2
                second_date = datetime(int(split_date_old[2]), int(split_date_old[1]), int(split_date_old[0]))
                years_old = (datetime.now() - second_date).days
                years_old = years_old / 365
                years_old = str(years_old).split('.')
                task5 = f'Возраст водителя: {years_old[0]} лет \n'
                print(task5)
                file_output.write(task5)
                print()

                task_data_na = 'Дата нарушения: 29.04.2021\n'
                file_output.write(task_data_na)

                cost = line_split[9].split(' ')
                cost = int(cost[1])
                task6 = f'Сумма выплат: {cost} \n\n'
                file_output.write(task6)


            file.close()
            file = open('enter.txt', mode='r')
            file_sorted = open('sorted.txt', mode='w')

            data_base = []
            for lines in file:
                line1 = lines.split('|')
                if 'ФИО' in line1[0]:
                    continue
                data_base.append(lines)

            violation = []
            for i in data_base:
                i = i.split('|')
                if i[8] not in violation:
                    violation.append(i[8])

            for i in violation:
                file_sorted.write(f'----------------------------------------------------\n'
                                  f'Нарушение: {i}\n')
                for line in data_base:
                    line = line.split('|')
                    if line[8] == i:
                        split_date = line[3].split('.')
                        first_date = datetime(int(split_date[2]), int(split_date[1]), int(split_date[0]))
                        stage_driver = (datetime.now() - first_date).days
                        stage_driver = str(stage_driver / 365).split('.')

                        line_split9 = line[9].split(' ')
                        cost = int(line_split9[1])
                        if int(stage_driver[0]) > 5:
                            cost = cost - cost / 100 * 10
                        elif int(split_date[0]) > 10:
                            cost = cost - cost / 100 * 20
                        elif int(split_date[0]) > 20:
                            cost = cost - cost / 100 * 30
                        elif int(split_date[0]) < 1:
                            cost = cost + cost / 100 * 10

                        output_text = f'Фамилия И.О: {line[0]}\n' \
                                      f'Номер водительского удостоверения: {line[2]}\n' \
                                      f'Стаж: {stage_driver[0]} лет\n' \
                                      f'Гос. номер: {line[4]}\n' \
                                      f'Штраф: {cost}\n\n'
                        file_sorted.write(output_text)
        elif task == 2:
            number_podpunkt = input('Введите номер подпункта: ')
            if number_podpunkt == '1':
                Fin = open('База2.txt', 'r', encoding='utf-8')
                info = Fin.readlines()
                Fin.close()
                for i in info:
                    Fin2 = open('База (второе задание).txt', 'a', encoding='utf-8')
                    Fin2.write(i)
            elif number_podpunkt == '2':
                Fin = open('База2.txt', 'r', encoding='utf-8')
                info = Fin.readlines()
                Fin2 = open('Сортировка по дате.txt', 'w', encoding='utf-8')
                Fin2.write('')
                Fin2 = open('Сортировка по дате.txt', 'a', encoding='utf-8')
                Fin2.write('Дата|Товар|Выручка\n')
                info = [line.rstrip() for line in info]
                Fin.close()
                v = []
                for i in info[1:]:
                    i = i.split()[0]
                    v.append(i)
                v = (sorted(v))
                prov = []
                for j in v:
                    wri = str('Дата: ' + j + '\n')
                    if wri not in prov:
                        Fin2.write(wri)
                    prov.append(wri)
                    for i in info[1:]:
                        I = i.split()[0]
                        if j == I and i.split()[1] not in prov:
                            prov.append(i.split()[1])
                            Fin2.write('  ' + i.split()[1] + ' ' + i.split()[2] + '\n')

            elif number_podpunkt == '3':
                Fin = open('База2.txt', 'r', encoding='utf-8')
                info = Fin.readlines()
                info = [line.rstrip() for line in info]
                Fin.close()
                Fin2 = open('Рейтинг.txt', 'w', encoding='utf-8')
                Fin2.write('')
                Fin2 = open('Рейтинг.txt', 'a', encoding='utf-8')
                v = []
                for i in info[1:]:
                    i = int(i.split()[2])
                    v.append(i)
                    v = (sorted(v, reverse=True))
                prov = []
                prov1 = []
                for j in v:
                    for i in info[1:]:
                        I = int(i.split()[2])
                        if j == I and i.split()[1] not in prov:
                            prov.append(i.split()[1])
                            prov1.append(i)
                prov = []
                for j in prov1:
                    j = str(j.split()[0])
                    wri = str('\nДата: ' + j + '\n')
                    if wri not in prov:
                        Fin2.write(wri)
                    prov.append(wri)
                    for i in prov1:
                        I = i.split()[0]
                        if j == I and i.split()[1] not in prov:
                            prov.append(i.split()[1])
                            Fin2.write('  ' + i.split()[1] + ' ' + i.split()[2] + '\n')
            elif number_podpunkt == '4':
                Fin = open('База для 4 задания.txt', 'r', encoding='utf-8')
                info = Fin.readlines()
                info = [line.rstrip() for line in info]
                Fin.close()
                Fin2 = open('Задание 4.txt', 'w', encoding='utf-8')
                Fin2.write('')
                Fin2 = open('Задание 4.txt', 'a', encoding='utf-8')
                v = []
                Year = []  # Массив сущетсвующих годов базы
                for i in info[1:]:
                    year = i.split()[0].split('.')[2]
                    if year not in Year:
                        Year.append(year)
                pom = []  # Массив для того, чтобы не повторялись объекты
                s = 0
                for y in Year:
                    Fin2.write(
                        '\n--------------------------------------------------------- ' + y + ' Год ----------------------------------------------------------------')
                    for m in range(1, 13):
                        Fin2.write('\n')
                        if len(str(m)) == 1:
                            Fin2.write('\n' + str(m) + ' месяц   ')
                        elif len(str(m)) == 2:
                            Fin2.write('\n' + str(m) + ' месяц  ')
                        for day in range(1, 26):
                            if len(str(s)) == 1:
                                Fin2.write(str(s) + '    ')
                            elif len(str(s)) == 2:
                                Fin2.write(str(s) + '   ')
                            elif len(str(s)) == 3:
                                Fin2.write(str(s) + '  ')
                            elif len(str(s)) == 4:
                                Fin2.write(str(s) + ' ')
                            s = 0

                            for i in info[1:]:
                                if int(i.split()[0].split('.')[1]) == m and y == (i.split()[0].split('.')[2]) and int(
                                        i.split()[0].split('.')[0]) == day:
                                    pom.append(m)
                                    s += int(i.split()[2])
                                elif int(i.split()[0].split('.')[1]) != m and m not in pom:
                                    pom.append(m)
                            if day == 25:
                                Fin2.write(str(s) + ' ')
            elif number_podpunkt == '5':
                Fin = open('База2.txt', 'r', encoding='utf-8')
                info = Fin.readlines()
                info = [line.rstrip() for line in info]
                Fin.close()
                Fin2 = open('Сортировка по прибыли.txt', 'w', encoding='utf-8')
                Fin2.write('')

                Fin2 = open('Сортировка по прибыли.txt', 'a', encoding='utf-8')
                v = []
                for i in info[1:]:
                    i = int(i.split()[2])
                    v.append(i)
                    v = (sorted(v, reverse=True))
                prov = []
                prov1 = []
                for j in v:
                    for i in info[1:]:
                        I = int(i.split()[2])
                        if j == I and i.split()[1] not in prov:
                            prov.append(i.split()[1])
                            prov1.append(i)
                month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                         "Ноябрь",
                         "Декабрь"]
                prov = []
                summ = 0
                max = 0
                min = (99999)
                for j in prov1:
                    j = str(j.split()[0])
                    wri = str('\nДата: ' + j)
                    if wri not in prov:
                        if summ != 0:
                            Fin2.write(str(summ) + ' рублей\n')
                        if summ > max:
                            max = summ
                            V = j
                        if summ < min and summ != 0:
                            min = summ
                            V1 = j
                        Fin2.write(wri + '\n')
                        summ = 0
                    prov.append(wri)
                    for i in prov1:
                        I = i.split()[0]
                        if j == I and i.split()[1] not in prov:
                            summ += int(i.split()[2])
                            prov.append(i.split()[1])
                            Fin2.write('  ' + i.split()[1] + ' ' + i.split()[2] + '\n')
                Fin2.write(str(summ) + ' рублей\n')
                if summ < min and summ != 0:
                    min = summ
                    V1 = j
                print('\nМаксимально прибыльный месяц: ' + month[int(V.split('.')[1])] + '. Прибыль составила:', max,
                      'рублей.')
                print('Минимально прибыльный месяц: ' + month[int(V1.split('.')[1])] + '. Прибыль составила:', min,
                      'рублей.')
    except:
        print('Ошибка!')
