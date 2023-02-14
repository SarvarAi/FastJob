from django.urls import path
from .views import HomeCV, HomeEmployer, UsersOperations, AboutUs

urlpatterns = [
    path('', HomeCV.as_view(), name='employee'),
    path('employer/', HomeEmployer.as_view(), name='employer'),
    path('about/', AboutUs.as_view(), name='about'),
    path('register/', UsersOperations.register, name='register'),
    path('login/', UsersOperations.login, name='login'),
]
