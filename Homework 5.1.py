def main() -> None:

    documents = [
        {
            "type": "passport",
            "number": "2207 876234",
            "name": "Василий Гупкин"
        },
        {
            "type": "invoice",
            "number": "11-2",
            "name": "Геннадий Покемонов"
        },
        {
            "type": "insurance",
            "number": "10006",
            "name": "Аристарх Павлов"
        }
    ]
 
    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [],
    }


    fl = True
    while fl:
        documents, directories = choose_manager(documents, directories)


def choose_manager(documents, directories):
    print('\nДоступные операции:\n'
          '|1| Найти человека по номеру документа\n'
          '|2| Найти полку, на которой находится докумет по его номеру\n'
          '|3| Вывести общий список документов\n'
          '|4| Добавить новый документ в хранилище\n'
          '|5| Удалить документ из каталога и его номер с полок\n'
          '|6| Переместить документ между полками\n'
          '|7| Добавить новую полоку\n')
    command = input('Введите номер команды: ')
    if command == '1':
        find_person(input('Введите номер документа: '), documents)
    elif command == '2':
        find_shelf(input('Введите номер документа: '), directories)
    elif command == '3':
        print_documents(documents)
    elif command == '4':
        number = input('\nВведите номер документа: ')
        document_type = input('\nВведите тип документа: ')
        name = input('\nВведите имя и фамилию владельца: ')
        shelf = input('\nВведите номер полки:')
        documents, directories = add_document(number, document_type, name, shelf, documents, directories)
    elif command == '5':
        delete_document(input('Введите номер документа: '), documents, directories)
    elif command == '6':
        number = input('\nВведите номер документа: ')
        shelf = input('\nВведите номер полки:')
        directories = move_document(number, shelf, directories)
    elif command == '7':
        directories = add_shelf(input('\nВведите номер полки:'), directories)
    else:
        print('\nОшибка ввода')

    return documents, directories


def find_person(number_of_documnet, documents):
    for document in documents:
        if number_of_documnet in document.values():
            print(f'\nВладелец документа с номером {number_of_documnet}: ', document['name'])


def find_shelf(number_of_documnet, directories):
    for shelf, number in directories.items():
        if number_of_documnet in number:
            print(f'\nДокумент номер {number_of_documnet} находится на полке: ', shelf)
            return 0
    print(f'Документ с номером {number_of_documnet} не существует')


def print_documents(documents):
    print('\nСписок документов: ')
    for document in documents:
        print(', '.join(document.values()))


def add_document(number, document_type, name, shelf, documents, directories):
    if shelf not in directories.keys():
        print(f'Полка с номером {shelf} не существует!')
        return documents, directories

    documents.append({'type': document_type, 'number': number, 'name': name})
    directories[shelf].append(number)

    return documents, directories

def delete_document(number, documents, directories):
    for value in directories.values():
        if number in value:
            value.remove(number)
    for document_info in documents:
        if number in document_info.values():
            documents.remove(document_info)
            return documents, directories
    print(f'Документ с номером {number} не существует!')
    return documents, directories


def move_document(number, shelf, directories):
    if shelf not in directories.keys():
        print(f'Полка с номером {shelf} не существует!')
        return directories
    for value in directories.values():
        if number in value:
            value.remove(number)
            directories[shelf].append(number)
            return directories
    print(f'Документ с номером {number} не существует!')
    return directories


def add_shelf(shelf, directories):
    if shelf in directories.keys():
        print(f'Полка с номером {shelf} уже существует!')
        return directories
    directories.update([(shelf, [])])
    return directories


if __name__ == '__main__':
    main()