from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exploration/',views.exploration_view, name='exploration')
]
