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


'''
# Data Insertion into Models: --> In 3 Ways
1. By creation of obj directly : (O/P format is Obj)
    e.g:
        obj=Dept(deptno=50,dname=20,loc='hyd')
    
2. With the help of create():   (O/P format is Obj)
    e.g:
        obj=Dept.objects.create(deptno=30,dname=20,loc='hyd')

3. With the help of get_or_create():    (O/P format is TUPLE (obj, bool)) --> bool is true if obj is not present else false
    e.g:
        >>> from app.models import *
        >>> dept_obj=Dept.objects.create(deptno=40,dname='civil',loc='Noida')
        >>> dept_obj
        <Dept: civil>
        >>> dept_obj1=Dept.objects.get_or_create(deptno=40)
        >>> dept_obj1
        (<Dept: civil>, False)
'''


'''
# Data Retrieving methods:

1.all()
2. get()
3. filter()

1.all(): TO fetch entire data from the model
    res=Model_name.objects.all()
    e.g:a=
         a=Dept.objects.all()
        >>> a
        <QuerySet [<Dept: cse>, <Dept: ECE>, <Dept: eee>, <Dept: civil>]>

2.get(): To fetch one obj(row) at a time based on specified cond
    res=Model_name.objects.get(field=val)
    e.g:
        a=Dept.objects.get(dname='cse')
        >>> a
        <Dept: cse>


3.filter(): To fetch multiple or zero or one obj's(rows) at a time based on specified cond
    res=Model_name.objects.get(filter_condition)
    e.g:
        a=Dept.objects.filter(deptno=10)
        >>> a
        <QuerySet [<Dept: cse>]>
        >>> a=Emp.objects.filter(deptno=10)
        >>> a
        <QuerySet [<Emp: pavi>, <Emp: sam>]>


'''



# Bonus and Salgrade Table
class Bonus(models.Model):

    ename=models.OneToOneField(Emp,on_delete=models.CASCADE)
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
        return self.pkp