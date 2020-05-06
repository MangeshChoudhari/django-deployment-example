from django import templates


register = templates.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(args,'')

# register.filter('cut',cut)
