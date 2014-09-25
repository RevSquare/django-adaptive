"""
Provide support for Cached loader.
Generate key for cached templates based on template names
and device type (desktop or mobile or tablet)
"""
from django.template.loaders.cached import Loader as CachedLoader
from django_adaptive.loader_utils import get_template_suffix


class AdaptiveTemplateCache(dict):

    def get_device(self):
        return get_template_suffix()

    def get_key(self, key):
        return key + self.get_device()

    def __getitem__(self, key):
        return super(AdaptiveTemplateCache, self).__getitem__(
            self.get_key(key))

    def __setitem__(self, key, value):
        return super(AdaptiveTemplateCache, self).__setitem__(
            self.get_key(key), value)


class Loader(CachedLoader):

    def __init__(self, loaders):
        super(Loader, self).__init__(loaders)
        self.template_cache = AdaptiveTemplateCache()
