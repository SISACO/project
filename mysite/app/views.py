from django.shortcuts import render

from . models import AlumniInfo

from . models import Activities

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
        selected_department = request.GET.get('department', '')
        
        if selected_department:
           alumni_department = AlumniInfo.objects.filter(department=selected_department)
        else:
           alumni_department = AlumniInfo.objects.all()
           
        selected_industry = request.GET.get('industry', '')
        
        if selected_industry:
           alumni_data = AlumniInfo.objects.filter(industry=selected_industry)
        else:
           alumni_data = AlumniInfo.objects.all()
        return render(request,'member.html', {'INDUSTRY_CHOICES': AlumniInfo.INDUSTRY_CHOICES, 'selected_industry': selected_industry,'DEPARTMENT_CHOICES': AlumniInfo.DEPARTMENT_CHOICES, 'selected_department': selected_department})
       
    
def activities(request):
        activities_posts=Activities.objects.all()
        return render(request,'activities.html',context={'activities_posts':activities_posts})
    
    
def alumni_list(request):
    alumni_data = AlumniInfo.objects.all()
    return render(request, 'alumni_list.html', {'alumni_data': alumni_data})


def alumni_list_department(request, department=None):
    if department:
        alumni_data = AlumniInfo.objects.filter(department=department)
    else:
        alumni_data = AlumniInfo.objects.all()

    return render(request, 'alumni_list_department.html', {'alumni_data': alumni_data, 'selected_department': department})






  