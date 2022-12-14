"""my_vbv_project URL Configuration

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
from VinylsBooksVideoGames.views import (show_vinyls, show_books, show_videogames, SearchItem, VinylAdd, BookAdd, VideogameAdd)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vinyls/', show_vinyls),
    path('books/', show_books),
    path('videogames/', show_videogames),
    path('vinyls/search', SearchItem.as_view()),
    path('vinyls/add', VinylAdd.as_view()),
    path('books/add', BookAdd.as_view()),
    path('videogames/add', VideogameAdd.as_view()),
]
