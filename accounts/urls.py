from django.urls import path

from .views import UserRegistrationView, UserLoginView, UserLogout

app_name = 'account'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]

