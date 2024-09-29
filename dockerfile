FROM python:3.9-slim 

# Ponhe o diretório num container
WORKDIR /app

# Copia os arquivos do diretório atual num container
COPY . /app

# Instala os pacotes listados no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Porta aonde o Flask app irá rodar( normalmente a 5000)
EXPOSE 5000

# Define o ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Roda a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]