from django import template

register = template.Library()


@register.filter
def placeholder(form_field, text):
    if hasattr(form_field, 'field'):
        form_field.field.widget.attrs['placeholder'] = text
    return form_field


@register.filter
def form_field_class(form_field, class_name):
    if hasattr(form_field, 'field'):
        default_classname = form_field.field.widget.attrs.get('class', '')
        form_field.field.widget.attrs['class'] = default_classname + ' ' + class_name
    return form_field


@register.filter
def form_field_styles(form_field, styles):
    if hasattr(form_field, 'field'):
        default_styles = form_field.field.widget.attrs.get('style', '')
        form_field.field.widget.attrs['style'] = default_styles + ' ' + styles
    return form_field
