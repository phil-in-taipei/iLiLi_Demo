from django.urls import path

from .views import join_form

app_name = 'join_info'
urlpatterns = [
    path('form/', join_form, name='form'),
    #path('register/', register, name='register'),
    #path('logout/', user_logout, name='logout'),
]