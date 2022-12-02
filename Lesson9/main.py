import telebot
from random import randint

global count
count = 0
print('Bot started')

bot = telebot.TeleBot(
    "", parse_mode=None)


def send_answer(answer, question_id):
    data = open("user_id.txt", "r", encoding="utf-8")
    user_id = data.readlines()
    data.close()
    answer_id = user_id[question_id]
    bot.send_message(answer_id, f'{answer}')


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
        if msg < num:
            bot.reply_to(message, 'Число должно быть выше')
            bot.register_next_step_handler(message, guessGame)
        elif num < msg:
            bot.reply_to(message, 'Число должно быть ниже')
            bot.register_next_step_handler(message, guessGame)
        elif num == msg:
            bot.reply_to(
                message, f'Поздравляю, Вы выиграли! Количество попыток: {count}')

    def helpDesk(message):
        user_id = str(message.from_user.id) + '\n'
        data = open('user_id.txt', 'a', encoding='utf-8')
        data.writelines(user_id)
        data.close()

        data = open('helpdesk.txt', "a", encoding="utf-8")
        data.writelines(
            f'{message.from_user.id} || {message.from_user.first_name}({message.from_user.username}) || {message.text}' + '\n')
        bot.send_message(message.from_user.id,
                         "Спасибо. Ваша заявка зарегистрирована.")

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
    elif message.text.lower() == "техподдержка":
        bot.reply_to(message, 'Опишите Вашу проблему в одном сообщении.')
        bot.register_next_step_handler(message, helpDesk)


bot.infinity_polling()
