'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'


def get_info():
    firstname = 'Иван'
    lastname = 'Иванов'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')

    return [firstname, lastname, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамиилия', 'Телефон'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def copy_line(current_file, destination_file, line_number):
    data = read_file(current_file)
    if 1 <= line_number <= len(data):
        line = data[line_number - 1]
        with open(destination_file, 'a', encoding='utf-8', newline='') as dest:
            f_w = DictWriter(dest, fieldnames=['Имя','Фамилия','Телефон'])
            f_w.writerow(line)
        print(f'Строка {line_number} скопирована')
    else:
        print('Неверный номер строки')

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                create_file(file_name)
            line_number = int(input('Введите номер строки для копирования: '))
            copy_line(file_name, 'copy.csv', line_number)


main()
