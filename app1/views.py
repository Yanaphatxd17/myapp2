from django.shortcuts import render
from .models import Student
import datetime

def index(request):
    context = {
        "Students": Student.objects.all(),
        "date": datetime.date.today(),
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {
        "student": student,
    }
    
    return render(request, "student_detail.html", context)