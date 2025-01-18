class MessagesHistory:
    def __init__(self):
        self.messagesHistory = {}
    
    def add_message(self, user_id, message, role):
        current_user_history = self.messagesHistory.get(user_id)
        
        if current_user_history:
            current_user_history.append({
                'role': role,
                'content': message,
            })

            if (len(current_user_history) > 8):
                del current_user_history[1:3]
        else:
            self.messagesHistory[user_id] = [{
                'role': role,
                'content': message,
            }]

    def get_user_history(self, user_id):
        user_history = self.messagesHistory.get(user_id)
        return user_history
    
    def clear_user_history(self, user_id):
        current_user_history = self.get_user_history(user_id)

        self.messagesHistory[user_id] = current_user_history[:1]
    
MessageHistoryInstance = MessagesHistory()