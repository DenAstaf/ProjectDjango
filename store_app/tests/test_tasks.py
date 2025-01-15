import pytest
from django.urls import reverse
from celery.result import AsyncResult
from store_app.tasks import log_add_product


@pytest.mark.django_db
def test_log_add_product_task(client):
    # Отправляет данные черрез форму
    response = client.post(reverse('add_product'), {
        'name': 'Bread',
        'description': 'Bread',
        'price': 30,
        'name_category': 'food',
    })

    assert response.status_code == 200

    task = log_add_product.delay('Bread')

    assert task.id is not None
