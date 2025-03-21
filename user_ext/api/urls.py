from django.urls import path
from . import controller


urlpatterns = [
    path('register', controller.Register.as_view()),
    path('login', controller.Login.as_view()),
    path('changeImage', controller.ChangeImage.as_view()),
    path('verifyToken', controller.TokenVerify.as_view()),

    path('report', controller.Reports.as_view()),

    path('more_info', controller.MoreInformation.as_view()),
    path('more_info/update/<id>', controller.UpdateMoreInformation.as_view()),
    path('hobbys', controller.Hobbys.as_view()),
    path('hobbys/update/<id>', controller.UpdateHobbys.as_view()),
    path('languages', controller.Languages.as_view()),
    path('languages/update/<id>', controller.UpdateLanguage.as_view()),
    path('references', controller.References.as_view()),
    path('references/update/<id>', controller.UpdateReference.as_view()),
    path('skills', controller.Skills.as_view()),
    path('skills/update/<id>', controller.UpdateSkills.as_view()),
    path('training', controller.Training.as_view()),
    path('training/update/<id>', controller.UpdateTraining.as_view()),
    path('work_experience', controller.WorkExperiences.as_view()),
    path('work_experience/update/<id>', controller.UpdateWorkExperience.as_view()),
]
