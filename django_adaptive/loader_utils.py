import os

from django.conf import settings
from .middleware import get_current_request

""" Setup constants with directories location prefixes, by default """
DESKTOP = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_DESKTOP', '')
TABLET = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_TABLET', '')
MOBILE = getattr(settings, 'ADAPTIVE_TEMPLATE_DIRECTORIES_MOBILE', '')


def get_template_suffix():
    """
    Returns template suffix based on settings and user agent used.
    """
    request = get_current_request()

    suffix = DESKTOP

    if hasattr(request, 'tablet') and request.tablet:
        suffix = TABLET

    elif hasattr(request, 'mobile') and request.mobile:
        suffix = MOBILE

    return suffix


def get_template_dirs(template_dirs):
    """
    Returns list of templates suffixed with appropriate string
    based on settings and user agent.
    """

    suffix = get_template_suffix()

    suffixed_dirs = [os.path.join(d, suffix) for d in template_dirs]

    return suffixed_dirs + list(template_dirs)
