
from datetime import datetime
from django.shortcuts import render ,redirect
from .models import Employee
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def Index(request):

    all_empy=Employee.objects.all()

    context={
        'emp':all_empy
    }


    return render(request,'all_Emp.html',context)

def add_emp(request):
    
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dept=request.POST['dept']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        role=request.POST['role']
        phone=request.POST['phone']
        

    
        empt=Employee(fname=fname,lname=lname,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())   
        empt.save()

        return redirect('/')



    return render(request,'add_emp.html')

def rem_emp(request,emp_id=0):
    if emp_id:
        
        emp_to_rem=Employee.objects.get(id=emp_id)
        emp_to_rem.delete()
    emp_rem=Employee.objects.all()

    context={
            'rem_emp':emp_rem
        }
        
    

    return render(request,'rem_emp.html',context)    

def flt_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            empss=emps.filter(Q(fname__icontains=name)|Q(lname__icontains=name))
        if dept:
            empss=emps.filter(dept=dept)
        if role:
          empss=emps.filter(role=role)

        print (empss)

    
 
    return render(request,'flt_emp.html')   
    # return HttpResponse ('heyy') 
