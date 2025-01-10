import pytest
from store_app.models import Category


@pytest.mark.django_db
def test_create_category(create_category):
    """
    Проверка на создание категории в БД,
    с помощью фикстуры 'create_category'
    """
    assert Category.objects.count() == 1  # проверка, что в бд был создан один объект


@pytest.mark.django_db
def test_read_category_(create_category):
    """Проверка на чтение категории из БД"""
    assert create_category.name_category == "Тестовая категория"


@pytest.mark.django_db
def test_update_category(create_category):
    """Проверка на апдейт категории в БД"""
    create_category.name_category = "Обновленная тестовая категория"
    create_category.save()

    obj_updated_category = Category.objects.get(id=create_category.id)
    assert obj_updated_category.name_category == "Обновленная тестовая категория"


@pytest.mark.django_db
def test_delete_category(create_category):
    """Проверка на удаление категории из БД"""
    create_category.delete()

    with pytest.raises(Category.DoesNotExist):
        Category.objects.get(id=create_category.id)
