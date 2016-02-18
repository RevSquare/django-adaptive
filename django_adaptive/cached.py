"""
Provide support for Cached loader.
Generate key for cached templates based on template names
and device type (desktop or mobile or tablet)
"""
from django.template.loaders.cached import Loader as CachedLoader
from django_adaptive.loader_utils import get_template_suffix


class Loader(CachedLoader):

    def cache_key(self, template_name, template_dirs):
        key = super(Loader, self).cache_key(template_name, template_dirs)
        return key + self.adaptive_get_key(key)

    def adaptive_get_device(self):
        return get_template_suffix()

    def adaptive_get_key(self, key):
        return key + self.adaptive_get_device()
