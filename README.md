Для запуска необходимо:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -m requirements.txt
4. Установить ollama (curl -fsSL https://ollama.com/install.sh | sh)
5. ollama pull llama3:latest
6. ollama pull mxbai-embed-large
7. в папке .config создать файл .env и прописать TG_API_KEY
8. python main.py
___
