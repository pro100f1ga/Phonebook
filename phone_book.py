def show_all(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()
            if not data:
                print("Телефонная книга пуста.")
            else:
                print(data)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def remove(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data = ""

    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        s = f"{last_name}, {first_name}, {patronymic}, {phone_number}\n"

    if s in data:
        data.remove(s)

        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(data)
    else:
        print("Запись не найдена.")


def modify(file_name: str):
    # print("Введите данные для поиска:\n")
    # last_name = input('Введите фамилию: ')
    # first_name = input('Введите имя: ')
    # patronymic = input('Введите отчество: ')
    # phone_number = input('Введите номер телефона: ')

    old_data = find_by_attribute(file_name, True)

    print("Введите новые данные:\n")
    last_name_ = input("Введите фамилию: ")
    first_name_ = input("Введите имя: ")
    patronymic_ = input("Введите отчество: ")
    phone_number_ = input("Введите номер телефона: ")
    data = ""
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f"{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n"

    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)


def find_by_attribute(file_name: str, option: bool):
    c = input("Введите 1 для поиска по фамилии, 2 для поиска по имени: ")

    opt = 0
    if c == "2":
        opt = 1

    attr = input("Введите имя/фамилию для поиска: ")
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        
        filtered_data = [line for line in data if line.split(", ")[opt] == attr]
        
        if not filtered_data:
            print("Нет записей с указанным именем/фамилией.")
            return None

        print(list(enumerate(filtered_data, start=1)))
        
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя: ")

        try:
            selected_data = filtered_data[int(id) - 1]
            return selected_data
        except IndexError:
            print("Неверный id.")
            return None
1


def add_new(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    if not (last_name and first_name and patronymic and phone_number):
        print("Ошибка: Все поля должны быть заполнены.")
        return

    with open(file_name, "a", encoding="utf-8") as fd:
        fd.write(f"{last_name}, {first_name}, {patronymic}, {phone_number}\n")
    
    print("Новая запись успешно добавлена.")


def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск записи по имени/фамилии')
        print('x - выход')
        
        answer = input('Введите операцию: ')
        
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_attribute(file_name, False))
        elif answer == 'x':
            flag_exit = True
        else:
            print('Ошибка: Некорректная операция. Пожалуйста, выберите правильный вариант.')

if __name__ == '__main__':
    main()
