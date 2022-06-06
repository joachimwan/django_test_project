from django import template
from django.contrib.auth.models import Group

register = template.Library()


# Custom template filter to check if user belongs to a group in django templates
@register.filter(name='has_group')
def has_group(user, group_name):
    # return user.groups.filter(name=group_name).exists()
    try:
        group = Group.objects.get(name=group_name)
    except Exception as e:
        print(e)
        return False
    return group in user.groups.all()
