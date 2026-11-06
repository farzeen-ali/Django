from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_form'),
    path('success/', views.feedback_success, name='feedback_success'),
]
