from django.db import models

# Create your models here.

# Department and Employee Table
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=10)
    loc=models.CharField(max_length=10)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=10)
    job=models.CharField(max_length=10)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Dept, on_delete=models.CASCADE)
    def __str__(self):
        return self.ename


# Bonus and Salgrade Table
class Bonus(models.Model):

    ename=models.CharField(max_length=10)
    job=models.CharField(max_length=10)
    sal=models.IntegerField()
    comm=models.IntegerField()
    bon_info=models.CharField(max_length=10)
    def __str__(self):
        return self.pk

class Salgrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()
    def __str__(self):
        return self.pk