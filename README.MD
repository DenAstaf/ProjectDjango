В данном проекте реализован Django с подключённой БД (субд - sqllite).<br>
Подключен Redis как брокер задач для Celery.

Реализован тест через pytest на проверку задач.<br>
запуск теста:<br> `pytest store_app/tests/test_tasks.py::test_log_add_product_task`

