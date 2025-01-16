from telebot import TeleBot
from modules.env import env;
from modules.llm import generate_response

def init_bot():
    bot = TeleBot(env.get('TG_API_KEY'))

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Здравствуйте, я могу Вам чем-нибудь помочь?")

    @bot.message_handler()
    def echo_message(message):
        response = generate_response(prompt=message.text)
        bot.reply_to(message, response)

    bot.infinity_polling()