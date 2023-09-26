import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6415923192:AAEHsmmTlGnqiV4NO9mzEY8dZ8-vitdPXs4')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Выслать фото', callback_data='photo')
    b2 = types.InlineKeyboardButton('Выслать аудио', callback_data='audio')
    markup.row(b1, b2)
    bot.send_message(message.chat.id, 'Выберите действие или введите команду', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'photo':
        bot.send_message(callback.message.chat.id, 'Введите запрос для фото: лес, горы, озеро, пустыня, город')
        bot.register_next_step_handler(callback.message, give_photo)
    if callback.data == 'audio':
        bot.send_message(callback.message.chat.id, 'Введите запрос для аудио: twice, blackpink, stayc, idle, aespa')
        bot.register_next_step_handler(callback.message, give_audio)


def give_photo(message):
    if message.text == 'лес':
        bot.send_photo(message.chat.id, "https://beautifoto.ru/wp-content/uploads/2019/07/5-7.jpg")
    elif message.text == 'горы':
        bot.send_photo(message.chat.id, "https://fikiwiki.com/uploads/posts/2022-02/1644860165_2-fikiwiki-com-p-kartinki-krasivikh-gor-3.jpg")
    elif message.text == 'озеро':
        bot.send_photo(message.chat.id, "https://traveltimes.ru/wp-content/uploads/2021/10/Zv8qYlir76I-1.jpg")
    elif message.text == 'пустыня':
        bot.send_photo(message.chat.id, "https://laplaya-rus.ru/wp-content/uploads/8/2/b/82b216dee419948ccbe6d7a2e4314553.jpeg")
    elif message.text == 'город':
        bot.send_photo(message.chat.id, "https://sportishka.com/uploads/posts/2022-04/1650719320_3-sportishka-com-p-megapolis-krasivo-foto-3.jpg")
    else:
        bot.send_message(message.chat.id, 'Несуществующий запрос')


def give_audio(message):
    if message.text == 'twice':
        audio = open(r'TWICE_-_I_CANT_STOP_ME_71397242.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'blackpink':
        audio = open(r'BLACKPINK_-_PLAYING_WITH_FIRE_65707358.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'stayc':
        audio = open(r'STAYC_-_RUN2U_74680679.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'idle':
        audio = open(r'I-DLE_-_Oh_my_god_69096668.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'aespa':
        audio = open(r'aespa_-_Black_Mamba_71686405.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, 'Несуществующий запрос')


@bot.message_handler(commands=['repository'])
def main(message):
    bot.send_message(message.chat.id, 'https://github.com/snmoonlight/SNLR1Bot.git')
    #webbrowser.open('https://github.com/snmoonlight/SNLR1Bot.git')


bot.polling(non_stop=True)
