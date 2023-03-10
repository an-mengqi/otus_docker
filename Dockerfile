# Устанавка базового образ
FROM python:3.10-alpine

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

ENV PATH="$PATH:/app/drivers/chromedriver_linux"

# Запуск тестов
ENTRYPOINT ["pytest"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]