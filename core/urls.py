
from django.contrib import admin
from django.urls import path, include
from core import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', include([
        path('', views.DashBoardIndex.as_view(), name='dashboard_index'),
        # path('edit/', views.edit),
    ])),
]