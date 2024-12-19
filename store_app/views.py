from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Product, Category
from .forms import ProductForm


class AllProductView(ListView):
    model = Product
    template_name = 'store_app/all_products.html'
    context_object_name = 'all_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context


class OneProductView(DetailView):
    model = Product
    pk_url_kwarg = 'pk'
    template_name = 'store_app/product_detail.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store_app/add_product.html'
    success_url = reverse_lazy('all_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление продуктов'
        return context


class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store_app/product_detail.html'
    success_url = reverse_lazy('all_products')

    def get_object(self, queryset=None):
        # Получаем объект продукта по его ID из URL
        return super().get_object(queryset)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукт'
        return context
