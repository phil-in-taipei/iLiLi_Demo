from django.urls import path

from .views import join_form, questionnaire_form, questionnaire_success

app_name = 'join_info'
urlpatterns = [
    #path('form/', join_form, name='form'),
    path('form/', questionnaire_form, name='form'),
    path('success/', questionnaire_success, name='success'),
]
