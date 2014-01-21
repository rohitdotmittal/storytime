#!/usr/bin/env python

from django import template
register = template.Library()

def get_items(myStr):
        items = [x.strip() for x in myStr.split(',')]
        return items[0:4]

register.filter('get_items', get_items)