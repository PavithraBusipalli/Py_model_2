from django.shortcuts import render
from app.models import *
# Create your views here.

def emp(request):
    EQLO=Emp.objects.all()
    d={'EQLO':EQLO}
    return render(request,'display_emp_data.html',d)

def dept(request):
    DQLO=Dept.objects.all()
    d={'DQLO':DQLO}
    return render(request,'display_data.html',d)
