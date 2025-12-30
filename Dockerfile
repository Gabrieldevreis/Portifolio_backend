# Imagem base com Python
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Dependências do sistema (opcional, mas recomendado)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala dependências do Python
RUN pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

# Porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
