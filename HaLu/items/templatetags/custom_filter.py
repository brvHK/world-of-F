# coding:utf-8

from datetime import date

from django import template

register = template.Library()
today = date.today()


@register.filter(name='is_new',expects_localtime=True)
def is_new(value):
    if type(value) is date:
        target_date = value
        diff = today - target_date
        return diff.days < 50
    else:
        return True 

register.filter('is_new', is_new)
