from telebot import TeleBot
from modules.env import env;
from modules.llm import generate_response
from modules.messagesHistory import MessagesHistory;

MessagesHistory = MessagesHistory()

def init_bot():
    bot = TeleBot(env.get('TG_API_KEY'))

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Здравствуйте, я могу Вам чем-нибудь помочь?")

    @bot.message_handler()
    def echo_message(message):
        user_id = message.from_user.id
        history = MessagesHistory.get_user_history(user_id)
        response = generate_response(prompt=message.text, history=history)
        MessagesHistory.add_message(user_id=user_id, user_message=message.text, bot_message=response)
        bot.reply_to(message, response)

    bot.infinity_polling()