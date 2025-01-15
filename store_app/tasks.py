from celery import shared_task


@shared_task
def log_add_product(product_name):
    message = f"Товар {product_name} добавлен!"
    print(message)  # Сообщение в консоль
    return message  # Возвращает сообщение, чтобы видеть его в задачах в админке
