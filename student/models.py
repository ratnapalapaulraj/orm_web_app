from django.db import models
from django.contrib import admin
# Create your models here.
class StudentDetail(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name")
    dob = models.DateField(help_text="Enter Date of Birth")
    age = models.IntegerField(help_text="Enter age from 18 to 22")
    course_name = models.CharField(max_length=100, help_text="Enter your course")
    department = models.CharField(max_length=100, help_text="Enter your department")
    reg_no = models.IntegerField(help_text="Enter your register number")

class StudentDetailAdmin(admin.ModelAdmin):
        List_display = ('name',
                        'dob',
                        'age',
                        'course_name',
                        'department',
                        'reg_no')