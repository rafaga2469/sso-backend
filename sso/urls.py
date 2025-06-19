from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CookieLoginView, CookieRefreshView, LogoutView, RegisterView, UserInfoView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/cookie/', CookieLoginView.as_view()),
    path('token/refresh/', CookieRefreshView.as_view()),
    path('me/', UserInfoView.as_view(), name='user_info'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
]
