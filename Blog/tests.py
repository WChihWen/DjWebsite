from django.test import TestCase
from django.contrib.auth.models import User
from .models import DjangoProject, Courses
from .forms import CoursesForm
from django.urls import reverse
# Create your tests here.

class DjangoProjectTest(TestCase):
    def setUp(self):
        self.djangoTitle = "Django Overview"
        self.djangoUrl = "https://docs.google.com/presentation/d/1XtD1DGIEf_IZ6jd2IIzoWVXAnKftAlrOvAXtV1Zg4u0/edit#slide=id.p"
        self.myDjango = DjangoProject(djangoprojectTitle = self.djangoTitle, djangoprojectUrl  = self.djangoUrl)
        
    def test_string(self):
        self.assertEqual(str(self.myDjango), 'Django Overview')
        
    def test_table(self):
       self.assertEqual(str(DjangoProject._meta.db_table), 'djangoproject')
       
class CoursesTest(TestCase):
    def setUp(self):
        self.courseTitle = "Web Programming W/ Python"
        self.courseSubject = "IT"
        self.courseCatalog = 112
        self.courseTerm = "2021 SPRING"
        self.courseUnits = 5.0
        self.courseInstructor = "Steven Conger"
        self.courseGrades = 0.0
        
        self.myCourse = Courses(courseTitle = self.courseTitle, courseSubject  = self.courseSubject, courseCatalog = self.courseCatalog, 
                                courseTerm= self.courseTerm, courseUnits=self.courseUnits, courseInstructor = self.courseInstructor, courseGrades = self.courseGrades)
        
    def test_string(self):
        self.assertEqual(str(self.myCourse), 'Web Programming W/ Python')
        
    def test_table(self):
       self.assertEqual(str(Courses._meta.db_table), 'courses')
       

# form test
class CoursesFormTest(TestCase):
    def test_CoursesForm(self):
        data = {
            'courseTitle': 'Web Programming W/ Python', 
            'courseSubject': 'IT', 
            'courseCatalog': 112, 
            'courseTerm': '2021 SPRING', 
            'courseUnits': 5.0,
            'courseInstructor': 'Steven Conger',
            'courseGrades': 0.0         
        }
        form = CoursesForm(data)
        self.assertTrue(form.is_valid)
       
       
     
 