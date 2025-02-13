from django.urls import path
from . import controller


urlpatterns = [
    path('register', controller.Register.as_view()),
    path('login', controller.Login.as_view()),
    path('changeImage', controller.ChangeImage.as_view()),
    path('verifyToken', controller.TokenVerify.as_view()),

    path('hobbys', controller.Hobbys.as_view()),
    path('languages', controller.Languages.as_view()),
    path('references', controller.References.as_view()),
    path('skills', controller.Skills.as_view()),
    path('training', controller.Training.as_view()),
    path('work_experience', controller.WorkExperiences.as_view()),
]