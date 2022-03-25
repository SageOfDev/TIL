"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include

from . import views
from django.conf import settings

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # .views
    re_path(r'^hello/$', views.hello),
    path('time/', views.current_datetime),
    re_path(r'^time/plus/(?P<offset>\d{1,2})/$', views.hours_ahead),
    path('browser/', views.ua_display),
    path('meta/', views.display_meta),
    path('contact/', views.contact),
    path('post/', views.post_list),

    # books
    path('books/', include('books.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('debuginfo/', views.debug)]
