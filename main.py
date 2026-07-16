import telebot
from telebot import types

TOKEN = '8989395405:AAETTO7WWMAEhxwR7I55670PGaZjhcqRsyc'
bot = telebot.TeleBot(TOKEN)

user_states = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Покупка 🛒"))
    return markup

def promo_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Ник 👤"))
    return markup

def actions_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Защитить 🛡️"))
    markup.add(types.KeyboardButton("Наблюдение 👁️"))
    markup.add(types.KeyboardButton("Бан 🚫"))
    return markup

@bot.message_handler(commands=['start'])
def start_cmd(message):
    user_states[message.chat.id] = "start"
    bot.send_message(
        message.chat.id, 
        "Привет! Нажми кнопку ниже для покупки доступа.", 
        reply_markup=main_menu()
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Покупка 🛒":
        user_states[chat_id] = "wait_promo"
        bot.send_message(chat_id, "Введите промокод для активации доступа:")
        return

    if user_states.get(chat_id) == "wait_promo":
        if text == "roblox26":
            user_states[chat_id] = "promo_activated"
            bot.send_message(
                chat_id, 
                "Бесплатный доступ на 3 дня(галочка)✅", 
                reply_markup=promo_menu()
            )
        else:
            bot.send_message(chat_id, "Неверный промокод. Попробуйте еще раз или нажмите 'Покупка 🛒'.", reply_markup=main_menu())
            user_states[chat_id] = "start"
        return

    if text == "Ник 👤" and user_states.get(chat_id) == "promo_activated":
        bot.send_message(
            chat_id, 
            "Выберите действие для этого пользователя:", 
            reply_markup=actions_menu()
        )
        return

    if text == "Защитить 🛡️" and user_states.get(chat_id) == "promo_activated":
        bot.send_message(chat_id, "✅")
        return

    if text == "Наблюдение 👁️" and user_states.get(chat_id) == "promo_activated":
        bot.send_message(chat_id, "ПК\nPoco x6 pro 5g\nRealme")
        return

    if text == "Бан 🚫" and user_states.get(chat_id) == "promo_activated":
        bot.send_message(chat_id, "Нужно оплатить 250 рублей")
        return

bot.infinity_polling()
