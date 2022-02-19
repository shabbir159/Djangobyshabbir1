from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("economic",views.economic,name='economic'),
    path("business",views.business,name='business'),
    path("account",views.account,name='account'),
    path("cs",views.cs,name='cs'),
    path("sc",views.secret,name='sc'),
    path("todolist",views.todo,name='todolist'),
    ]