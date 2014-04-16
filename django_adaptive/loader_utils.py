import os
import threading

from django.conf import settings

""" Setup constants with directories location prefixes, by default """
DESKTOP = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_DESKTOP', '')
TABLET = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_TABLET', '')
MOBILE = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_MOBILE', '')


def ParseTemplateName(template_name):
    """
    Adds the prefix to a template name using the django request object.
    """
    thread_locals = threading.local()
    request = getattr(thread_locals, 'request', None)
    prefix = DESKTOP

    if hasattr(request, 'mobile') and request.mobile:
        prefix = MOBILE
    elif hasattr(request, 'tablet') and request.tablet:
        prefix = TABLET

    return os.path.join(prefix, template_name)
