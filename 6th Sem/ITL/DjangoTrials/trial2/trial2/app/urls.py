from django.urls import path
from . import views

urlpatterns = [
    path('category',views.category,name='category'),
    path('result',views.result,name = 'result')
    ]
