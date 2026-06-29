from django.urls import path
from . import views  # This belongs here, because home has a views.py!

urlpatterns = [
    path('', views.home, name='home'),
    path('treatment/<slug:slug>/', views.treatment_detail, name='treatment_detail'),
]