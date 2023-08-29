import telebot
import extensions
import Exchange_bot_token

token = Exchange_bot_token.set_token()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def starter(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}! "
                                      f"В случае необходимости этото бот поможет узнать "
                                      f"актуальные курсы валюты, подсчитает стоимость "
                                      f"тех или иных активов и так далее.")
    bot.send_message(message.chat.id, f"Вот список команд для бота с пояснениями \n"
                                      f"/help - справка \n"
                                      f"/value - список валют их стоимость в ₽\n\n"
                                      f"Так же, бот может расчитать стоимость некоторого количества "
                                      f"одной из доступных валют в рублях, для этого, отправте боту "
                                      f"сообщение формата: <Название валюты> <Количество>.\n"
                                      f"Например: Фунт 200\n\n"
                                      f"Кроме того, он умеет ковертировать одну валюту в другую. "
                                      f"Для этого отправте боту сообщение формата: "
                                      f"<Название конвертируемой валюты> <Название валюты в которую хотите "
                                      f"конвертировать> <Количество>\n "
                                      f"Например: Доллар Фунт 200\n\n"
                                      f"`Названия валют в именительном падеже, с большой буквы")


@bot.message_handler(commands=['help'])
def helper(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Вот список команд для бота с пояснениями \n"
                                      f"/help - справка \n"
                                      f"/value - список валют их стоимость в ₽\n\n"
                                      f"Так же, бот может расчитать стоимость некоторого количества "
                                      f"одной из доступных валют в рублях, для этого, отправте боту "
                                      f"сообщение формата: <Название валюты> <Количество>.\n"
                                      f"Например: Фунт 200\n\n"
                                      f"Кроме того, он умеет ковертировать одну валюту в другую. "
                                      f"Для этого отправте боту сообщение формата: "
                                      f"<Название конвертируемой валюты> <Название валюты в которую хотите "
                                      f"конвертировать> <Количество>\n "
                                      f"Например: Доллар Фунт 200\n\n"
                                      f"`Названия валют в именительном падеже, с большой буквы")

@bot.message_handler(commands = ["value"])
def valute_value(message: telebot.types.Message):
    valute_value_dict = extensions.RequesterCore.get_me_price_my_thral()
    bot.reply_to(message, f"Вот список доступных валют и их стоимость в рублях за одну единицу \n")
    text = ""
    for row in extensions.thrals_dict.keys():
        r = extensions.thrals_dict.get(row)
        f = f"{row} {valute_value_dict.get(r)} ₽"
        text = "\n".join((text, f))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def exchange(message: telebot.types.Message):
    try:
        text_list = []
        for row in message.text.split(" "):
            text_list.append(row)
            for row in text_list:
                for row2 in extensions.fuuu_list:
                    if not row.find(row2):
                        raise extensions.FuuuExeption
        if len(text_list) < 2:
            raise extensions.NotEnoughExeption
        if len(text_list) > 3:
            raise extensions.MoreThenEnoughExeption
        if len(text_list) == 2:
            if not text_list[1].isdigit():
                raise extensions.SyntaxExeption
            if text_list[0] not in extensions.thrals_dict.keys():
                raise extensions.SyntaxExeption
            bot.reply_to(message, f"{text_list[1]} {text_list[0]} в рублях: \n"
                                  f"Это где-то: {extensions.RequesterCore.convert_it_my_thral(text_list[0],int(text_list[1]))}₽")
        if len(text_list) == 3:
            if not text_list[2].isdigit():
                raise extensions.SyntaxExeption
            if text_list[0] not in extensions.thrals_dict.keys()\
                    or text_list[1] not in extensions.thrals_dict.keys():
                raise extensions.SyntaxExeption
            bot.reply_to(message, f"{text_list[2]} {text_list[0]} в {text_list[1]}: \n"
                                  f"Это где-то: {extensions.RequesterCore.exchange_it_my_thral(text_list[0],text_list[1],int(text_list[2]))}")
    except extensions.APIExeption as e:
        bot.reply_to(message, e)



bot.polling(none_stop=True)