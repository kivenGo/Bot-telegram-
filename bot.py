import telebot

bot = telebot.TeleBot("5705202999:AAGZAyzcFBnIFGcLaqPFO0wopevJo_f9M-4")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to my bot!")

bot.polling()
