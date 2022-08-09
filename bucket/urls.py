from django.urls import path, register_converter

from .views import BasketItemCreateListAPIView,BasketUpdateDeleteAPIView, DashboardAPIView, FilterBasketByDate, GetAllBasketsDates, PeriodicTaskPerDay, SearchBucketItemsAPIView
from .utils import DateConverter

register_converter(DateConverter,'date')

urlpatterns = [
    path('item/',BasketItemCreateListAPIView.as_view()),
    path('item/<int:pk>',BasketUpdateDeleteAPIView.as_view()),
    path('filter/<date:date>', FilterBasketByDate.as_view()),
    path('get-dates/', GetAllBasketsDates.as_view()),
    path('dashboard/<date:date>', DashboardAPIView.as_view()),
    path('search/',SearchBucketItemsAPIView.as_view()),
    path('periodic-task/',PeriodicTaskPerDay.as_view()),
]