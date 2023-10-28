from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from colorfield.fields import ColorField


class Recipe(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=100
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=500
    )

    cooking_steps = models.TextField(
        verbose_name='Шаги приготовления',
        max_length=10000)

    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления (в минутах)',
        default=30,
        validators=[MinValueValidator(
            1,
            message='Время приготовления не может быть меньше одной минуты'
        ), MaxValueValidator(
            600,
            message='Время приготовления не может быть больше десяти часов')]
    )

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images'
    )

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    color = ColorField(
        format='hex',
        verbose_name='HEX-код',
        max_length=7,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'


class CategoryRecipe(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'category: {self.customer.name} -> price: {self.recipe.title}'