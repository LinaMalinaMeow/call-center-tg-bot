import ollama
from modules.messages_history import MessageHistoryInstance
from modules.template import get_prompt_with_template

MIN_DISTANCE = 185

def generate_response(prompt, user_id):
    prompt_template = get_prompt_with_template(prompt)

    if (MessageHistoryInstance.get_user_history(user_id) is None):
        MessageHistoryInstance.add_message(user_id=user_id, message=prompt_template, role='user')
        MessageHistoryInstance.add_message(user_id=user_id, message=prompt, role='user')
    else:
        MessageHistoryInstance.add_message(user_id=user_id, message=prompt, role='user')

    llm_response = ollama.chat(
        model='llama3:latest',
        messages=MessageHistoryInstance.get_user_history(user_id)
    )

    llm_response_message = llm_response.message.content

    MessageHistoryInstance.add_message(user_id=user_id, message=llm_response_message, role='assistant')

    return llm_response_message