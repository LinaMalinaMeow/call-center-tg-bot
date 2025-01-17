from modules.vectorstore import search_knowledge_base

MIN_DISTANCE = 185

def get_prompt_with_template(prompt):
    rag = search_knowledge_base(prompt)
    distances = rag['distances'][0]
    condition_distance_indexes = []

    for i in range(0, len(distances)):
        if (distances[i] < MIN_DISTANCE):
            condition_distance_indexes.append(i);
    
    rag_docs = rag.get('documents')[0]
    docs_for_context = []

    for i in range(len(rag_docs)):
        if (i in condition_distance_indexes):
            docs_for_context.append(rag_docs[i])
    
    context = ''
    for doc in docs_for_context:
        context = context + doc + '\n'

    prompt_template = """
        Ты консультант в клинике, тебе задают вопросы, отвечай на эти вопросы опираясь на информацию,
        которая находится ниже в теге "<context>", если ответа на вопрос нет в информации, но он относится к клинике или медицине,
        тогда извиняйся и предлагай клиенту
        обратиться на горячую линию по телефону +7-999-999-99-99.
        Если ты понимаешь, что вопрос не относится к клинике, медицине, отвечай, что ты консультируешь только по вопросам клиники, 
        не нужно предлагать звонить на горячую линию клиники.
        Отвечай на вопросы кратко и четко, без лишней информации.
        Общайся максимально вежливо и уважительно, не показывай и не рассказывай,
        что ты нейросеть и у тебя есть какой-то контекст и теги. Ты можешь только отвечать на вопросы.
        Вопрос на который тебе нужно ответить находится в теге <question>.
        <context>
        {}
        </context>
        Вопросы я буду отсылать тебе в следующих сообщениях, отвечай всегда на русском языке, пиши грамотно
    """.format(context)

    return prompt_template