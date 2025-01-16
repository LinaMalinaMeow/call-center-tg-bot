class MessagesHistory:
    def __init__(self):
        self.messagesHistory = {}

    def add_message(self, user_id, user_message, bot_message):
        current_user_history = self.messagesHistory.get(user_id)

        if current_user_history:
            current_user_history.append({
                'user_message': user_message,
                'bot_message': bot_message
            })
            if (len(current_user_history) > 5):
                current_user_history.pop(0)
        else:
            self.messagesHistory[user_id] = [{
                'user_message': user_message,
                'bot_message': bot_message
            }]

    def get_user_history(self, user_id):
        user_history = self.messagesHistory.get(user_id)
        s = ''

        if (user_history is not None):
            for i in user_history:
                s = s + f'user: {i['user_message']}; your answer: {i['bot_message']}\n'

        return s