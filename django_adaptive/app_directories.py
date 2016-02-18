from django.template.loaders.app_directories import Loader \
        as AppDirectoriesLoader
from .loader_utils import get_template_dirs

try:
    from django.template.loaders.app_directories import app_template_dirs
except ImportError:
    from django.template.utils import get_app_template_dirs
    app_template_dirs = get_app_template_dirs('templates')



class Loader(AppDirectoriesLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        if template_dirs is None:
            template_dirs = app_template_dirs

        dirs = get_template_dirs(template_dirs)

        return super(Loader, self).get_template_sources(template_name, dirs)
