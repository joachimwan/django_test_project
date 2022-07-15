# Generated by Django 4.0.2 on 2022-07-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_project_options'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='phase',
            constraint=models.UniqueConstraint(fields=('well', 'name'), name='unique_phase'),
        ),
    ]