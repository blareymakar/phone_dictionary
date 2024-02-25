#Формат хранения данных:Имя Номер Коммент

# 1. Показать все контакты
def show_all(my_dict, output_string="Выводим на экран телефонный справочник:"):
    empty="                    "
    print(output_string)
    print("Имя                 |Телефон             |Комментарий")
    print("_____________________________________________________")
    for i in my_dict:
        empty_name = empty[len(i['Имя']):]
        empty_phone = empty[len(i['Телефон']):]
        print(f"{i['Имя'].title()}{empty_name}|{i['Телефон'].title()}{empty_phone}|{i['Комментарий'].title()}")

# 2. Добавить контакт
def add_contact(my_dict):
    print("Добавляем контакт в файл:")
    name=input("Введите имя:\n").lower()
    phone=input("Введите номер телефона:\n").lower()
    comment=input("Введите комментарий:\n").lower()
    new_string=f'\n{name} {phone} {comment}'
    my_dict.append({'Имя':name, 'Телефон':phone, 'Комментарий':comment})
    with open('phone_numbers.txt', 'a') as file:
        file.write(new_string)
    show_all(my_dict)

# 3. Найти контакт
def find_contact(my_dict):
    counter=0
    search_word=input("Введите текст для поиска контакта:\n")
    for list_item in my_dict:
        double = False
        for value in list_item.values():
            if double == False:
                if search_word in value:
                    double = True
                    print(f"{list_item['Имя'].title()}   {list_item['Телефон'].title()}   "
                          f"{list_item['Комментарий'].title()}")
                    counter+=1
    if counter:
        print("Текст " + search_word + " встречается в " + str(counter) +" записи/записях")
    else:
        print("Совпадений в телефонном справочнике не найдено")

# 4. Изменить контакт
def change_contact(my_dict):
    print("Вы выбрали изменить контакт. Выводим все контакты:")
    show_all(my_dict,'')
    contact_to_change = input("Введите имя контакта, который нужно изменить:\n").lower()
    with open('phone_numbers.txt', 'r') as file:
        found = False
        for line in file:
            words=line.split()
            if contact_to_change in words:
                line_to_change = line
                found = True
    if not found:
        print(f"Контакт {contact_to_change} в файле не найден\n")
    else:
        while True:
            try:
                field_to_change=int(input("В какое поле вносим изменения: 1. Имя 2. Телефон 3. Комментарий?\n"))
                if field_to_change in (1,2,3):
                    break
                else:
                    print("Вы ввели неверное значение. Выберите пункт из меню")
            except ValueError:
                print("Вы ввели неверное значение. Выберите пункт из меню")
                next

        new_value=input("Введите новое значение поля:\n").lower()
        if new_value!='':
            words = line_to_change.split()
            words[field_to_change-1]=new_value
            changed_line = ' '.join(words)+'\n'
            with open('phone_numbers.txt', 'r') as file:
                lines = file.readlines()
            with open('phone_numbers.txt', 'w') as file:
                for line in lines:
                    if line == line_to_change:
                        file.write(changed_line)
                    else:
                        file.write(line)
            print("Изменения внесены!")
        else:
            print("Вы ничего не ввели!")

# 5. Удалить контакт
def remove_line(my_dict):
    print("Вы выбрали удалить контакт. Выберите контакт из списка ниже")
    show_all(my_dict,'')
    contact_to_remove = input("Введите имя контакта, который нужно удалить\n").lower()
    with open('phone_numbers.txt', 'r') as file:
        found = False
        for line in file:
            words=line.split()
            if contact_to_remove in words:
                print(f'Найден контакт: {line} - удаляем...')
                line_to_remove = line
                found = True
    if not found:
        print(f"Контакт {contact_to_remove} в файле не найден\n")
    else:
        with open('phone_numbers.txt', 'r') as file:
            lines = file.readlines()

        with open('phone_numbers.txt', 'w') as file:
            for line in lines:
                if line != line_to_remove:
                    file.write(line)




menu=(1,2,3,4,5,6)
menu_item = 1

while menu_item!=6:
    print("""        Меню программы:
    ________________________
    1. Показать все контакты
    2. Добавить контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Завершение программы
    
    Выберите нужный пункт меню:""")


    while True:
        try:
            menu_item=int(input())
            if menu_item in menu:
                break
            else:
                print("Вы ввели неверное значение. Выберите пункт из меню")
        except ValueError:
            print("Вы ввели неверное значение. Выберите пункт из меню")
            next
    phone_book = []
    with open('phone_numbers.txt', 'r') as file:
        for each_string in file:
            phone_book.append({'Имя': each_string.split()[0].lower(),
                               'Телефон': each_string.split()[1].lower(),
                               'Комментарий': each_string.split()[2].lower()})
    if menu_item==1:
        show_all(phone_book)
    elif menu_item==2:
        add_contact(phone_book)
    elif menu_item==3:
        find_contact(phone_book)
    elif menu_item==4:
        change_contact(phone_book)
    elif menu_item==5:
        remove_line(phone_book)

    if menu_item!=6:
        input("\nНажмите Enter для продолжения")
else:
    print("Конец программы")
