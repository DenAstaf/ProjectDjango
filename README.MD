В данном проекте реализован Django с подключённой БД (субд - sqllite).<br>
Подключен Redis как брокер задач для Celery:<br>
При отправке данных через форму, будет выполнена задача.

**Чтобы запустить с оболочки необходимо:**<br>
1. Запустить сервера Redis
2. Запустить Celery worker в новом окне терминала через команду:

`celery -A myproject worker --loglevel=info -P solo (на Windows)`
`celery -A myproject worker --loglevel=info (на Linux)`

3. Запустить Джанго: `python manage.py runserver`

Реализован тест через pytest на проверку задач.<br>
Запуск теста:<br> `pytest store_app/tests/test_tasks.py::test_log_add_product_task`


**Чтобы запустить с Docker-а, а не с оболочки необходимо:**<br>
1. Изменить в seetings.py:<br>
С:<br>
	`CELERY_BROKER_URL = 'redis://localhost:6379/0'  # для запуска с оболочки`
На:<br>
	`CELERY_BROKER_URL = 'redis://redis:6379/0'  # для запуска с докера`
2. Выполнить команду: `docker-compose up –build`
3. Если выдает ошибку, удалить в проекте виртуальное окружение, папку `.venv` и повторить пункт 2.