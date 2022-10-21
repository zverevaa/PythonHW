# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

import bot_dictionary as bot


phrase = input(
    'Для начала разговора с ботом скажите "Привет", для окончания разговора с ботом, в любой момент скажите "Пока": ')

while phrase.lower() != 'пока':
    print(bot.dictionary.get((phrase.lower()), 'Извините, я Вас не понимаю'))
    phrase = input('Бот ожидает Вашего ответа: ')
print(bot.dictionary.get((phrase.lower())))