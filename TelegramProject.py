import telebot

bot = telebot.TeleBot('5153504793:AAG9CNv-bj8zWRr1U9uLy4z_lklZZGzL7wM')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет, солнце. Я создал этот чат для тебя, как понятно из названия "Хотел сделать приятное"<b>',parse_mode='html')


bot.polling(none_stop=True)