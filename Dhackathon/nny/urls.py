from django.urls import path
from .views import *

app_name = 'nny'

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password_change/', PasswordChangeView.as_view()),
    path('trains/', TrainListView.as_view()),
    path('trains/<int:pk>', TrainDetailView.as_view()),
    path('seats/', SeatListView.as_view()),
    path('seats/<int:pk>', SeatDetailView.as_view()),
    path('usedeye/', UsedEyeView.as_view()),
    path('eye/', EyeView.as_view()),
    path('warning/', WarningView.as_view()),
]