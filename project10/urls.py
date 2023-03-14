"""project10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('If_condition/',If_condition,name='If_condition'),
    path('If_else_condition/',If_else_condition,name='If_else_condition'),
    path('If_elif_condition/',If_elif_condition,name='If_elif_condition'),
    path('Nested_condition/',Nested_condition,name='Nested_condition'),
    path('for_loop/',for_loop,name='for_loop'),
]
