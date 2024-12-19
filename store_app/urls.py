from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllProductView.as_view(), name='all_products'),
    path('add-product/', views.AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/', views.EditProductView.as_view(), name='edit_product'),
]
