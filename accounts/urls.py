from django.urls import path 
from .views import (
    index,  # Add index view
    CitizenSignupView, CitizenSigninView, InstituteSignupView, InstituteSigninView, 
    CitizenSignupAPI, CitizenSigninAPI, InstituteSignupAPI, InstituteSigninAPI
)

urlpatterns = [
    # Index page
    path('', index, name='index'),  # Add this line

    # Template-based views
    path('citizen/signup/', CitizenSignupView, name='citizen_signup'),
    path('citizen/signin/', CitizenSigninView, name='citizen_signin'),
    path('institute/signup/', InstituteSignupView, name='institute_signup'),
    path('institute/signin/', InstituteSigninView, name='institute_signin'),

    # API endpoints (kept for reference)
    path('api/citizen/signup/', CitizenSignupAPI.as_view(), name='api_citizen_signup'),
    path('api/citizen/signin/', CitizenSigninAPI.as_view(), name='api_citizen_signin'),
    path('api/institute/signup/', InstituteSignupAPI.as_view(), name='api_institute_signup'),
    path('api/institute/signin/', InstituteSigninAPI.as_view(), name='api_institute_signin'),
]
