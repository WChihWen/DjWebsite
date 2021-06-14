from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('java/', views.java, name="java"),
    path('python/', views.python, name="python"),
    path('sorting/', views.sorting, name="sorting"),
    path('django/', views.django, name="django"),
    path('course/', views.course, name="course"),
    path('coursedetails/<int:id>', views.coursedetails, name="coursedetails"),  
    path('newCourse/', views.newCourse, name="newCourse"),   
    path('loginmessage/', views.loginmessage, name="loginmessage"),   
    path('logoutmessage/', views.logoutmessage, name="logoutmessage"),       
]