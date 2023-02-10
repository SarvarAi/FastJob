from django.urls import path
from .views import HomeCV, HomeEmployer, user_login


urlpatterns = [
    path('', HomeCV.as_view(), name='employee'),
    path('employer/', HomeEmployer.as_view(), name='employer'),
    path('login/', user_login, name='login'),
]
