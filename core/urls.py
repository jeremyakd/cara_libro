from django.urls import path
from core.views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', views.sample, name="sample"),
]
