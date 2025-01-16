import ollama
from modules.vectorstore import search_knowledge_base

def generate_response(prompt, history):
    rag = search_knowledge_base(prompt)
    print(rag)
    rag_docs = rag.get('documents')[0]

    context = ''
    for doc in rag_docs:
        context = context + doc + '\n'

    prompt = """
        Ты консультант в клинике, тебе задают вопросы, отвечай на эти вопросы опираясь на информацию,
        которая находится ниже в теге "<context>", если ответа на вопрос нет в информации, тогда извиняйся и предлагай клиенту
        обратиться на горячую линию по телефону +7-999-999-99-99.
        Если ты понимаешь, что вопрос не относится к клинике, медицине, отвечай, что ты консультируешь только по вопросам клиники.
        Отвечай на вопросы кратко и четко, без лишней информации.
        Общайся максимально вежливо и уважительно, не показывай и не рассказывай, что ты нейронка и у тебя есть какой-то контекст.
        Вопрос на который тебе нужно ответить находится в теге <question>.
        <context>
        {}
        </context>
        <question>{}</question>
    """.format(context, prompt)


    llm_response = ollama.generate(
        model = 'llama3:latest',
        prompt=prompt
    )

    return llm_response['response']