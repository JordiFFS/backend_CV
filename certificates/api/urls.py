from django.urls import path
from . import controller

urlpatterns = [
    path('new', controller.NewCertificate.as_view()),
    path('update/<id>', controller.UpdateCertificate.as_view()),

]