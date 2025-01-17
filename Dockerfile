# Указываем базовый Python
FROM python:3.13.0

# Устанавливает переменные окружения для оптимизации поведения Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#Устанавливает рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливает Poetry.
RUN pip install poetry

# Отключает создание виртуальных окружений, т.е Poetry устанавливает зависимости в глобальное окружение контейнера, а не в отдельное виртуальное окружение
RUN poetry config virtualenvs.create false

# Копирует файлы pyproject.toml и poetry.lock для установки зависимостей (./ - текущая рабочая директория)
COPY poetry.lock pyproject.toml ./

# Устанавливает зависимости, используя Poetry
RUN poetry install --no-root

# Копирует остальной исходный код приложения
COPY . .

# Команда для запуска сервера
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
