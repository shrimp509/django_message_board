"""message_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from account.apis import register, login
from board.apis import post, comment

api_path = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(api_path + 'register/', register),
    path(api_path + 'register', register),

    path(api_path + 'login/', login),
    path(api_path + 'login', login),

    path(api_path + 'board/post/', post),
    path(api_path + 'board/post', post),

    path(api_path + 'board/post/<int:post_id>/comment/', comment),
    path(api_path + 'board/post/<int:post_id>/comment', comment),
]
