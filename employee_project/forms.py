from django  import forms
from .models import Employee,EmpSalary

class Employee1(forms.ModelForm):
      class Meta:
          model= Employee
          fields = "__all__"


class EmpSalary(forms.ModelForm):
      class Meta:
          model= EmpSalary
          fields = ('Employee_salary',)


