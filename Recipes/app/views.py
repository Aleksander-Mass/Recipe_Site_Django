from django.contrib.auth import login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .serializers import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from app.forms import RecipeForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('user_login')
    template_name = 'registration.html'


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_view.html', {'recipe': recipe})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']

            recipe = Recipe()

            recipe.title = title
            recipe.description = description
            recipe.cooking_steps = cooking_steps
            recipe.cooking_time = cooking_time
            recipe.image = image
            recipe.author = request.user
            recipe.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = RecipeForm()

    return render(request, 'add_recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']

            recipe.title = title
            recipe.description = description
            recipe.cooking_steps = cooking_steps
            recipe.cooking_time = cooking_time
            recipe.image = image
            recipe.author = request.user
            recipe.save()

            return HttpResponseRedirect(reverse('index'))
        else:
            message = 'Что-то пошло не так...'
    else:
        message = 'Заполните форму'
        form = RecipeForm({
            'title': recipe.title,
            'description': recipe.description,
            'cooking_steps': recipe.cooking_steps,
            'cooking_time': recipe.cooking_time,
            'image': recipe.image,
        })

    return render(request, 'edit_recipe.html', {'form': form, 'message': message})


def authenticate_user(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user


def auth(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate_user(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'auth.html', {'form': form, 'error': 'Аккаунт неактивен'})
            else:
                return render(request, 'auth.html', {'form': form, 'error': 'Неверные данные для входа'})
    else:
        form = UserLoginForm()
    return render(request, 'auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    recipes = Recipe.objects.all()[:5]
    return render(request, 'index.html', {'recipes': recipes})