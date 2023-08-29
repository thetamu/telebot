import telebot

TOKEN = "5714364860:AAE8KfQf70G8CvWLAJ2vSMX5g7FKfrDt2f0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def handle_docs_audio(message: telebot.types.Message):
    bot.reply_to(message, f"Nice meme XD, {message.chat.username}")

bot.polling(none_stop=True)
