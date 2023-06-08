from bot import bot,check_subs,markup

@bot.message_handler(commands=['start'])
def start(m):
    if check_subs(m):
        bot.send_message(m.chat.id,f"Salom {m.from_user.first_name}")

bot.infinity_polling()