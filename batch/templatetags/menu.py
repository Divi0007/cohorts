from django import template

from batch.models import agegroup, days

register = template.Library()

@register.inclusion_tag('core/menu.html')
def menu():
    agegroups = agegroup.objects.all()
    day=days.objects.all()

    return {'agegroups': agegroups,'days':day}
@register.inclusion_tag('core/vmenu.html')
def vacant():
    agegroups = agegroup.objects.all()
    day=days.objects.all()

    return {'agegroups': agegroups,'days':day}