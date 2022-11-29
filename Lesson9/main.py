import telebot
from random import randint

global count
count = 0
print('Bot started')

bot = telebot.TeleBot(
    "", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def bot_body(message):
    def calc(message):
        bot.reply_to(
            message, f'Результат: {eval(message.text)}')

    def guessGame(message):
        msg = int(message.text)
        global count
        count += 1
        print(num)
        if msg < num:
            bot.reply_to(message, 'Число должно быть выше')
            bot.register_next_step_handler(message, guessGame)
        elif num < msg:
            bot.reply_to(message, 'Число должно быть ниже')
            bot.register_next_step_handler(message, guessGame)
        elif num == msg:
            bot.reply_to(
                message, f'Поздравляю, Вы выиграли! Количество попыток: {count}')

    if message.text.lower() == 'игра':
        msg = bot.reply_to(
            message, "Бот загадал число от 1 до 1000, попытайтесь его угадать!")
        num = randint(1, 1000)
        global count
        count = 0
        bot.register_next_step_handler(msg, guessGame)
    elif message.text.lower() == "калькулятор":
        msg = bot.reply_to(
            message, "Введите выражение, которое необходимо посчитать")
        bot.register_next_step_handler(msg, calc)


bot.infinity_polling()
# def gameStart(message):
#     bot.reply_to(message, "Бот загадал число, попытайтесь его угадать!")
#     randomNumber()
#     bot.register_next_step_handler(message, guessGame)
