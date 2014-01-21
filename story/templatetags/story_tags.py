#!/usr/bin/env python

from django import template
register = template.Library()

@register.simple_tag
def get_image(myStr):
        image = myStr.split(',')
        return image[0]

@register.simple_tag
def get_items(myStr):
        items = myStr.split(',')
        return items[0:4]
