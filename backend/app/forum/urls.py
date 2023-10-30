"""
URL configuration for forum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from advertisements.views import (announcement_create, announcement_detail, add_comment_to_announcement,
                                  announcement_list, announcement_edit, announcement_delete)


urlpatterns = [
    path('', announcement_list, name='home'),
    path('announcement/new/', announcement_create, name='announcement_create'),
    path('announcement/<int:pk>/', announcement_detail, name='announcement_detail'),
    path('announcement/<int:pk>/comment/', add_comment_to_announcement, name='add_comment_to_announcement'),
    path('announcement/<int:pk>/edit/', announcement_edit, name='announcement_edit'),
    path('announcement/<int:pk>/delete/', announcement_delete, name='announcement_delete'),
]