import os
from celery import Celery

# Устанавливает переменную окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создает экземпляр Celery
app = Celery('config')

# Загружает настройки Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит задачи в приложениях Django
app.autodiscover_tasks()
