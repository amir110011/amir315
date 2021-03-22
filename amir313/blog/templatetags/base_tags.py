from django import template
from ..models import Category

register = template.Library()
@register.simple_tag
def title():
    return "وبلاگ امیر نبوی"


@register.inclusion_tag("blog/partials/categoty_navbar.html")
def categoty_navbar():
    return {
        "cat": Category.objects.filter(status=True)
    }

