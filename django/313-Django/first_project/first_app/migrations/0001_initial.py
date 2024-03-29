# Generated by Django 5.0.2 on 2024-02-28 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('start_date', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.department')),
            ],
        ),
    ]
