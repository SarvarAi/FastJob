from django.urls import path
from .views import HomeCV, HomeEmployer


urlpatterns = [
    path('', HomeCV.as_view(), name='employee'),
    path('employer/', HomeEmployer.as_view(), name='employer'),
]
