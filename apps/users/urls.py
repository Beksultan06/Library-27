from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.views import UserAPI, UserRegisterAPI

router = DefaultRouter()
router.register(r'register', UserRegisterAPI, basename='register')
router.register(r'list-user', UserAPI, basename='user')

urlpatterns = [
    
]

urlpatterns += router.urls