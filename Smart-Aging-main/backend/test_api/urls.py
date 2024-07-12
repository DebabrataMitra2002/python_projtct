"""
URL configuration for iot_server project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path("type", views.index, name="avg"),
    path("type/date", views.avg_by_date, name="avg_by_date"),
    path("tpa/predict/", views.predict_two_people, name="predict_two_people"),
    path("opa/predict/", views.predict_one_people, name="predict_one_people"),
    path("motion/", views.insert_motion_data, name="insert_motion_data"),
]
