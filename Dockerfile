# Imagem base
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Código do projeto
COPY . .

# Comando correto para Railway
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn setup.wsgi:application --bind 0.0.0.0:8000
