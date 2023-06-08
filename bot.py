from telebot import TeleBot,types
import os
bot=TeleBot(token=os.getenv('BOT_TOKEN'),parse_mode="MARKDOWN")
markup=types.InlineKeyboardMarkup()
markup.add(
    types.InlineKeyboardButton("SunniFan kanali","https://t.me/sunnifan"),
    types.InlineKeyboardButton("WHAT IF...? AGARDA...? kanali","https://t.me/what_if_agarda")
)
def check_subs(m):
    if m.chat.type=='private':
        if bot.get_chat_member("@sunnifan",id) and bot.get_chat_member("@what_if_agarda",id):
            return True
        bot.send_message(m.chat.id,f"{m.from_user.first_name} quyidagi kanallarga obuna bo'ling")
        bot.delete_message(m.chat.id,m.id)
        return False
    return True