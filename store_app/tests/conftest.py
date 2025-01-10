import pytest
from store_app.models import Category


@pytest.fixture
def create_category():
    """Фикстура, создает объект в БД"""
    return Category.objects.create(name_category="Тестовая категория")


