# Базовый образ Python
FROM python:3.10-slim

# Установка зависимостей для PostgreSQL и других библиотек
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
