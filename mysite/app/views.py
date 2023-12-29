from django.shortcuts import render

from . models import AlumniInfo

# Create your views here.
def index(request):
    computer_count = AlumniInfo.objects.filter(department='computer_department').count()
    civil_count = AlumniInfo.objects.filter(department='civil_department').count()
    mechanical_count = AlumniInfo.objects.filter(department='mechanical_department').count()
    automobile_count = AlumniInfo.objects.filter(department='automobile_department').count()
    electronics_count = AlumniInfo.objects.filter(department='electronics_department').count()
    electrical_count = AlumniInfo.objects.filter(department='electrical_department').count()
    return render(request,'index.html', {'computer_count': computer_count,'civil_count': civil_count,'mechanical_count': mechanical_count,'automobile_count': automobile_count,'electronics_count': electronics_count,'electrical_count': electrical_count,})

def member(request):
        return render(request,'member.html')
    
def activities(request):
        return render(request,'activities.html')
    
def add_alumini(request):
        return render(request,'add_alumini.html')
    
def alumni_list(request):
    alumni_data = AlumniInfo.objects.all()
    return render(request, 'alumni_list.html', {'alumni_data': alumni_data})


def alumni_list_department(request, department=None):
    if department:
        alumni_data = AlumniInfo.objects.filter(department=department)
    else:
        alumni_data = AlumniInfo.objects.all()

    return render(request, 'alumni_list_department.html', {'alumni_data': alumni_data, 'selected_department': department})






  