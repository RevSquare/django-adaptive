from django.template.loaders.app_directories import Loader \
    as AppDirectoriesLoader, app_template_dirs

from .loader_utils import get_template_dirs


class Loader(AppDirectoriesLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        if template_dirs is None:
            template_dirs = app_template_dirs

        dirs = get_template_dirs(template_dirs)

        return super(Loader, self).get_template_sources(template_name, dirs)
