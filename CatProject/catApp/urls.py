from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListCat.as_view()), name='cat_list'),
    path('<int:pk>/', views.DetailCat.as_view()), name='cat_detail'),
]
