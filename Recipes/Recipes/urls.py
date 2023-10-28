from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from app import views
from app.views import SignUpView
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('user_login/', views.auth, name='user_login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('recipe_view/<int:recipe_id>', views.recipe_view, name='recipe_view'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('logout_view/', views.logout_view, name='logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)