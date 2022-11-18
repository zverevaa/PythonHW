contacts = ['Иванов Иван Иванович',
            'Васильев Василий Васильевич', 'Антонова Антонина Антоновна']
phone_numbers = ['+7925668905', '+79157648809', '+79268450920']


def printPhoneNumbers():
    results = []
    for i in range(len(contacts)):
        results.append(f'{contacts[i]} : {phone_numbers[i]}')
    return '\n'.join(results)


def newContact():
    name = input('Пожалуйста, введите ФИО нового контакта: ')
    phone_number = input(
        'Пожалуйста, введите номер телефона нового контакта: ')
    contacts.append(name)
    phone_numbers.append(phone_number)
    return f'Контакт {contacts[len(contacts)-1]} с телефоном {phone_numbers[len(phone_numbers)-1]} был успешно создан'


def searchByName():
    name = input('Пожалуйста, введие ФИО: ')
    for i in range(len(contacts)):
        if (name == contacts[i]):
            return f'{contacts[i]} : {phone_numbers[i]}'
    else:
        return 'Такого контакта нет в базе данных'
