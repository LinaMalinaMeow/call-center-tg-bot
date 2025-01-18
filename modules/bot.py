from telebot import TeleBot
from modules.env import env;
from modules.llm import generate_response
import os
from modules.parse_audio import parse_audio
from modules.messages_history import MessageHistoryInstance

def init_bot():
    bot = TeleBot(env.get('TG_API_KEY'))

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Здравствуйте, я могу Вам чем-нибудь помочь?")

    @bot.message_handler(commands=['clear'])
    def clear_context(message):
        user_id = message.from_user.id

        MessageHistoryInstance.clear_user_history(user_id)
        
        bot.reply_to(message, 'Контекст разговора был сброшен!')

    @bot.message_handler()
    def echo_message(message):
        user_id = message.from_user.id
        print(MessageHistoryInstance.get_user_history(user_id), '\n\n\n')

        response = generate_response(prompt=message.text, user_id=user_id)

        bot.reply_to(message, response)

    @bot.message_handler(content_types=['voice'])
    def echo_audio_message(message):
        user_id = message.from_user.id

        file_info = bot.get_file(message.voice.file_id)
        result = parse_audio(file_info)
        if result is False:
            false_message = 'Извините, я не могу распознать ваше голосовое сообщение.'
            bot.send_message(message.from_user.id, false_message)
            return
        bot.send_message(message.from_user.id, generate_response(prompt=result, user_id=user_id))

    bot.infinity_polling()