from django.urls import path
from .views import MahsulotListCreate, MahsulotRetrieveUpdateDestroy, ChegirmaListCreate, BuyurtmaListCreate, \
    BuyurtmaDetail

urlpatterns = [
    path('mahsulotlar/', MahsulotListCreate.as_view()),
    path('mahsulotlar/<int:pk>/', MahsulotRetrieveUpdateDestroy.as_view()),
    path('chegirmalar/', ChegirmaListCreate.as_view()),
    path('buyurtmalar/', BuyurtmaListCreate.as_view()),
    path('buyurtmalar/<int:pk>/', BuyurtmaDetail.as_view()),
]
