# Generated by Django 5.0.4 on 2024-04-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('b', 'B'), ('m', 'M'), ('ph', 'PH')], default='b', max_length=20),
        ),
    ]
