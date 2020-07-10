from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("LogIn/",views.LogIn,name="LogIn"),
    path("complaint_locations/",views.get_complaint_location,name="complaint_locations"),
    path("home/",views.HomePage,name ="home"),
    path("signOut/",views.sign_out,name="signOut"),
    path('analysis_page/',views.analysisHome,name="analysis_page"),
]
