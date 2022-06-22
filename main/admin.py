from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Well)
admin.site.register(Phase)
admin.site.register(Step)
admin.site.register(Lookahead)
admin.site.register(Sequence)
