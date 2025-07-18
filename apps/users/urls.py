from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.views import UserAPI, UserRegisterAPI, LoginAPIView

router = DefaultRouter()
router.register(r'register', UserRegisterAPI, basename='register')
router.register(r'list-user', UserAPI, basename='user')

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name='login')
]

urlpatterns += router.urls