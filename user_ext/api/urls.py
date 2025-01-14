from django.urls import path
from . import controller


urlpatterns = [
    path('register', controller.Register.as_view()),
    path('login', controller.Login.as_view()),
    path('changeImage', controller.ChangeImage.as_view()),
    path('verifyToken', controller.TokenVerify.as_view()),
]