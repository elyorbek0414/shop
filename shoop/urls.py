from django.urls import path
from .views import MahsulotListCreate, ChegirmaListCreate, BuyurtmaListCreate

urlpatterns = [
    path('mahsulotlar/', MahsulotListCreate.as_view()),
    path('chegirmalar/', ChegirmaListCreate.as_view()),
    path('zaqazlar/', BuyurtmaListCreate.as_view()),
]
