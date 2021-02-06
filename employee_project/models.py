from django.db import models

# Create your models here.
class Employee(models.Model):
    CATEGORY=(
        ('Python','Python'),
        ('Php','Php'),
        ('Java','Java'),
        ('Node','Nodes')
    )
    Employee_id=models.AutoField
    Employee_name=models.CharField(max_length=100)
    Employee_department=models.CharField(max_length=100,choices=CATEGORY)



class EmpSalary(models.Model):
    EmployeeSalary_id=models.AutoField
    Employee_id=models.ForeignKey('Employee', on_delete=models.CASCADE)
    Employee_salary=models.IntegerField(default=0)