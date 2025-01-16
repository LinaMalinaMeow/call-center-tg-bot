Для запуска необходимо:
1. source .venv/bin/activate
2. pip install -m requirements.txt
3. Установить ollama (curl -fsSL https://ollama.com/install.sh | sh)
4. ollama pull llama3:latest
5. ollama pull mxbai-embed-large
6. в папке .config создать файл .env и прописать TG_API_KEY
7. python main.py
___
