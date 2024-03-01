from django.db import models

class Department(models.Model):
	dept_id = models.CharField(max_length=5, primary_key=True)
	dept_name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 30)

	def __str__(self):
		return self.dept_name
	
class Employee(models.Model):
	emp_id=models.AutoField(primary_key = True)
	emp_name=models.CharField(max_length=30)
	dept=models.ForeignKey(Department, on_delete=models.CASCADE)
	age=models.IntegerField()
	start_date=models.DateField()

	def __str__(self):
		return self.emp_name