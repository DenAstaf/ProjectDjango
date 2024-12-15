from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название продукта')
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    name_category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name_category = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    description = models.TextField()

    def __str__(self):
        return self.name_category
