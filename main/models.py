from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-last_modified']


class Well(models.Model):
    name = models.CharField(max_length=30, unique=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name="wells")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="wells")

    def __str__(self):
        return self.name


class Phase(models.Model):
    name = models.CharField(max_length=30)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name="phases")
    order = models.PositiveIntegerField(null=True)  # order of phases within a well

    def __str__(self):
        return f'{self.well} - {self.order} - {self.name}'

    class Meta:
        ordering = ['well', 'order']


class Step(models.Model):
    ops_step = models.CharField(max_length=100)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name="ops_steps")
    order = models.PositiveIntegerField(null=True)  # order of steps within a phase

    def __str__(self):
        return f'{self.phase} - {self.order} - {self.ops_step}'

    class Meta:
        ordering = ['phase__well', 'phase__order', 'order']


class Lookahead(models.Model):
    name = models.CharField(max_length=30, default="Lookahead")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="lookaheads")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="lookaheads")

    def __str__(self):
        return f'{self.name} - {self.project}'


class Sequence(models.Model):
    lookahead = models.ForeignKey(Lookahead, on_delete=models.CASCADE, null=True, blank=True, related_name="sequence")
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True)  # order of phases within a lookahead

    def __str__(self):
        return f'{self.lookahead} - {self.order} - {self.phase}'

    class Meta:
        ordering = ['lookahead', 'order']
