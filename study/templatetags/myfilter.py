from django import template
from django.utils.safestring import SafeData, mark_safe
from django.utils.text import (
    Truncator, normalize_newlines, phone2numeric, slugify as _slugify, wrap,
)
from django.utils.html import (
    avoid_wrapping, conditional_escape, escape, escapejs,
    json_script as _json_script, linebreaks, strip_tags, urlize as _urlize,
)
from django.utils.text import (
    Truncator, normalize_newlines, phone2numeric, slugify as _slugify, wrap,
)
from functools import wraps
register = template.Library()
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.replace('\n',"<br>")
register.filter('lower', lower)

def stringfilter(func):
    """
    Decorator for filters which should only receive strings. The object
    passed as the first positional argument will be converted to a string.
    """
    def _dec(*args, **kwargs):
        args = list(args)
        args[0] = str(args[0])
        if (isinstance(args[0], SafeData) and
                getattr(_dec._decorated_function, 'is_safe', False)):
            return mark_safe(func(*args, **kwargs))
        return func(*args, **kwargs)

    # Include a reference to the real function (used to check original
    # arguments by the template parser, and to bear the 'is_safe' attribute
    # when multiple decorators are applied).
    _dec._decorated_function = getattr(func, '_decorated_function', func)

    return wraps(func)(_dec)


@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def linebreaksbr(value, autoescape=True):
    """
    Convert all newlines in a piece of plain text to HTML line breaks
    (``<br>``).
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
        return mark_safe((value.replace('\n', '<br>')).title())

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def tabindent(value, autoescape=True):
    """
    Convert all newlines in a piece of plain text to HTML line breaks
    (``<br>``).
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    return mark_safe(value.replace('  ', '&nbsp&nbsp'))

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def title(value,autoescape=True):

    return mark_safe(value.title())

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def secretm(value, autoescape=True):
    a='abcdefghijklmnopqrstuvwxyz'
    def hidden(i):
        result=''
        for i in i:
            if i == ' ':
                result+=i
                continue
            try:
                ind=a.index(i.lower())
            except:
                result+=i
                continue
            if ind <= 13:
                result+=a[-(ind+1)]
            elif ind >= 14:
                result+=a[len(a)-ind-1]
        return result
    return mark_safe(hidden(value))
