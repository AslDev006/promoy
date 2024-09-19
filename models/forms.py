from django import forms
from .models import ProductModel, AdviceModel


class AdviceForm(forms.ModelForm):
    class Meta:
        model = AdviceModel
        fields = ['name', 'address', 'phone_number', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'