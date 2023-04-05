from django.urls import path
from . import views
app_name='css'

urlpatterns = [
    path ('master/',views.get_master, name="master"),
    path('home/',views.get_home, name="home"),
    path('courses/',views.get_courses, name="courses"),
    path('contact/',views.get_contact, name="contact")
]