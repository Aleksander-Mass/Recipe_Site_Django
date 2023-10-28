from django import forms
from app.models import Recipe


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Название рецепта'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Описание рецепта'}))

    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                  'placeholder': 'Шаги приготовления'}))

    cooking_time = forms.IntegerField(min_value=1, max_value=600, widget=forms.NumberInput(attrs={'class':'form-control',
                                                                                                  'placeholder': 'Время приготовления (в минутах)'
                                                                                                  }))
    image = forms.ImageField()
