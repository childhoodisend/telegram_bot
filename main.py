import telebot
import сrypto
import db

bot = telebot.TeleBot("1526975295:AAH_eg829onohdx_lO7-QnMfSXNFJTj4CD0")


@bot.message_handler(commands=['start'])
def send_welcome(message):

    db.insert_into_table(message.chat.id, message.chat.username)


    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('get', 'stop', 'start')

    bot.reply_to(message, message.chat.first_name + ", hello!", reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def send_stop(message):
    bot.send_message(message.chat.id, "Good bye! \U000026C4")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Yep, I'm @pahpan's first bot")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text.lower() == 'start':
        send_welcome(message)
        # bot.send_sticker(259129417,  'CAACAgIAAxkBAAKrvF_8hYSWMxFP3J-OZ9E-0ly3W1YvAAJLAANSiZEjyG1ozT_o2useBA')
    if message.text.lower() == 'stop':
        send_stop(message)
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

    if message.text.lower() == 'get':
        data = сrypto.get_data_json()
        bot.send_message(message.chat.id, str(data))


bot.polling(none_stop=False, interval=0, timeout=20)
