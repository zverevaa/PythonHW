import model


def createMenu():
    print('Добро пожаловать в телефонный справочник.')
    print('')
    print('Для вывода всего справочника введите 1')
    print('Для создания новой записи введите 2')
    print('Для поиска по ФИО введите 3')
    print('Для выхода из справочника введите 0')
    print('')
    printOption()


def getOption():
    option = input('Пожалуйста, введите число: ')
    return option


def printOption():
    for option in iter(getOption, '0'):
        match option:
            case '1':
                print(model.printPhoneNumbers())
            case '2':
                print(model.newContact())
            case '3':
                print(model.searchByName())
