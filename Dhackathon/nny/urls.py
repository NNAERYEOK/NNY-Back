from django.urls import path
from .views import *

app_name = 'nny'

urlpatterns = [
    path('trains/', TrainListView.as_view()),
    path('trains/<int:pk>', TrainDetailView.as_view()),
    path('seats/', SeatView.as_view()),
]