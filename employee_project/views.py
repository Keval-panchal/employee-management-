from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import render
from .models import Employee
from .forms import Employee1
# Create your views here.
def Employee_add(request):
    form = Employee1()
    if request.method == 'POST':
        form=Employee1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/views')

    
    return  render (request,"employee_management/employee_insert.html" ,{'form':form})

def Employee_view(request):
    Employees=Employee.objects.all()
    print(Employee)
    return  render (request,"employee_management/employee_view.html",{'Employees':Employees}) 
  
def Employee_delete(request,id):
    Employees=Employee.objects.get(id=id)
    Employees.delete()
    return redirect('/views')


def Employee_update(request,id):
     form = Employee1()
     Employees={'form':form}
     return  render(request,"employee_management/employee_insert.html",Employees)