from django.shortcuts import render, get_object_or_404
from .models import User, DjangoProject, Courses
from django.urls import reverse_lazy
from .forms import CoursesForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'Blog/index.html')

def aboutme(request):
    return render(request,'Blog/aboutme.html')

def java(request):
    return render(request,'Blog/java.html')

def python(request):
    return render(request,'Blog/python.html')

def sorting(request):
    return render(request,'Blog/sorting.html')

def django(request):
    return render(request,'Blog/django.html', {'django_list': DjangoProject.objects.all()})

def course(request):
    return render(request,'Blog/course.html', {'course_list': Courses.objects.all()})

def coursedetails(request, id):
    return render(request, 'Blog/coursedetails.html', {'course_list': get_object_or_404(Courses, pk=id)})

@login_required
def newCourse(request):
    form = CoursesForm    
    if request.method == 'POST':
        form  = CoursesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = CoursesForm
    else:
        form = CoursesForm        
    return render(request,'Blog/newcourses.html', {'form': form})

def loginmessage(request):
    return render(request,'Blog/loginmessage.html')

def logoutmessage(request):
    return render(request,'Blog/logoutmessage.html')
