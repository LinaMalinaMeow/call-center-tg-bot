from modules.vectorstore import init_knowledge_base
from modules.bot import init_bot

def main():
    print('bot started')

    init_knowledge_base()
    init_bot()

main()