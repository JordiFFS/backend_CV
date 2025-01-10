from django.urls import path
from . import controller

urlpatterns =[
    path('cbx/gender', controller.ComboBoxGender.as_view()),
    path('cbx/levelStudy', controller.ComboBoxLevelStudy.as_view()),
    path('cbx/countryResidence', controller.ComboBoxCountryResidence.as_view()),
    path('cbx/professionalTitle', controller.ComboBoxProfessionalTitle.as_view()),
]