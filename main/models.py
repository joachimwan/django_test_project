from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.project_name


class Well(models.Model):
    well_name = models.CharField(max_length=30, unique=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name="project")

    def __str__(self):
        return self.well_name
