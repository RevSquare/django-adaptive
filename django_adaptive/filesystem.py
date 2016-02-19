from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.conf import settings

from .loader_utils import get_template_dirs


class Loader(FilesystemLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        if template_dirs is None:
            if settings.TEMPLATES:
                template_dirs = self.engine.dirs
            elif settings.TEMPLATE_DIRS:
                template_dirs = settings.TEMPLATE_DIRS

        dirs = get_template_dirs(template_dirs)

        return super(Loader, self).get_template_sources(template_name, dirs)
