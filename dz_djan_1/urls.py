from t_list.views import current_datetime
from django.urls import path, include

"""dz_djan_1 URL Configuration

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
from t_list.views import (
    ZadachaListView,
    ZadachaCreateView,
    ZadachaUpdateView,
    ZadachaDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("time/", current_datetime),
    path("data/", ZadachaListView.as_view()),
    path("data_crt/", ZadachaCreateView.as_view()),
    path("data_upd/<int:pk>", ZadachaUpdateView.as_view()),
    path("data_del/<int:pk>", ZadachaDeleteView.as_view()),
    path("api/", include("t_list.urls")),
]
