from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_plan/', views.add_plan, name='add_plan'),
    path('query_plan/', views.query_plan, name='query_plan'),
    path('query_result/', views.query_result, name='query_result'),
]