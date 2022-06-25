from django.contrib import admin
from .models import *

# Register your models here.


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Project._meta.concrete_fields if field.name != "id"]
#
#
# admin.site.register(Project, ProjectAdmin)


model_list = [
    Project,
    Well,
    Phase,
    Step,
    Lookahead,
    Sequence,
]

for m in model_list:
    class Admin(admin.ModelAdmin):
        list_display = [field.name for field in m._meta.concrete_fields if field.name != "id"]

    admin.site.register(m, Admin)
