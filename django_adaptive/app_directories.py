from django.template.loaders.app_directories import Loader \
    as AppDirectoriesLoader

from .loader_utils import ParseTemplateName


class Loader(AppDirectoriesLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        return super(Loader, self)\
            .get_template_sources(ParseTemplateName(template_name),
                                  template_dirs)
