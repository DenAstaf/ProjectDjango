from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=200,
        label='Название товара',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
        error_messages={
            'required': 'Обязательное поле для заполнения.'
        }
    )

    description = forms.CharField(
        label='Описание товара',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание товара'})
    )

    price = forms.FloatField(
        label='Цена товара',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену товара'}),
        min_value=0.0,
        error_messages={
            'required': 'Обязательное поле для заполнения.'
        }
    )

    name_category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Обязательное поле для заполнения.'
        }
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'name_category']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.isupper():
            raise forms.ValidationError('Название продукта должно быть с большой буквы.')
        return name
