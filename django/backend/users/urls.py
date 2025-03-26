from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup_api'),
    path('api/login/', LoginView.as_view(), name='login_api'),
    path('api/logout/', LogoutView.as_view(), name='logout_api'),
]
