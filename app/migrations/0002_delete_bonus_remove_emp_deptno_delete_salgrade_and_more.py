# Generated by Django 4.2.7 on 2023-12-11 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bonus',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='deptno',
        ),
        migrations.DeleteModel(
            name='Salgrade',
        ),
        migrations.DeleteModel(
            name='Dept',
        ),
        migrations.DeleteModel(
            name='Emp',
        ),
    ]
