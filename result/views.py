from django.shortcuts import render
from result.models import Result_Data
# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        school=request.POST['school']
        rollno=request.POST['rollno']
        gender=request.POST['gender']
        bengali=request.POST['bengali']
        english=request.POST['english']
        mathematic=request.POST['mathematic']
        physics=request.POST['physics']
        chemistry=request.POST['chemistry']
        biology=request.POST['biology']
        ins =Result_Data(name=name,school=school,rollno=rollno,gender=gender,bengali=bengali,english=english,mathematic=mathematic,physics=physics,chemistry=chemistry,biology=biology)
        ins.save()
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')