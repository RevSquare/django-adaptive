###############
Django Adaptive
###############

Manages to load templates according to the type of device to a specific directory prefix.

These loaders work with the django-mobi app. Please read the documentation for more information: https://pypi.python.org/pypi/django-mobi

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

From PyPi

.. code-block::  shell-session

    pip  install django-adaptive

From Github

.. code-block::  shell-session

    -e git+https://github.com/RevSquare/django-adaptive#egg=django-adaptive

*****
Setup
*****

Before starting, make sure you have correctly setup django-mobi: https://pypi.python.org/pypi/django-mobi

Django adaptive basicaly overwrites django default filesystem and app_directories loaders. You can pick the overwritten loader you want to use separately and use them concurently with the former django loaders.

The first step is to add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'django_adaptive'
        ...
    )

Then you will need to declare the loaders you want to add in your settings.py file

.. code-block::  python

    TEMPLATE_LOADERS = (
        'django-adaptive.filesystem.Loader',
        'django-adaptive.app_directories.Loader',
        #'django.template.loaders.filesystem.Loader',
        #'django.template.loaders.app_directories.Loader',
    )

Final step is to add ThreadLocal Middleware

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'mobi.middleware.MobileDetectionMiddleware',
        'django_adaptive.middleware.ThreadLocals',
        ...
    )
    
******************************
Declaring your device prefixes
******************************

At this stage nothing will be done. You need to specify the directories for each device categories in your settings.py.

The settings constants are:

* ADAPTIVE_TEMPLATE_DIRECTORIES_DESKTOP
* ADAPTIVE_TEMPLATE_DIRECTORIES_TABLET
* ADAPTIVE_TEMPLATE_DIRECTORIES_MOBILE


Usage exemple:

.. code-block::  python

    import os

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    PROJECT_PATH = os.path.join(os.path.dirname(__file__), '..')
    
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_PATH, 'templates')
    )
    
    ADAPTIVE_TEMPLATE_DIRECTORIES_MOBILE = 'mobile'

This code will install the templates for mobile in the *templates/mobile* directory. And the rest of the files in *templates* (by default no prefix is added).

In case you would need to combine devices type in a similar directory, you just need to point them to it. For exemple:

.. code-block::  python

    ADAPTIVE_TEMPLATE_DIRECTORIES_DESKTOP = 'desktop'
    ADAPTIVE_TEMPLATE_DIRECTORIES_TABLET = 'mobile'
    ADAPTIVE_TEMPLATE_DIRECTORIES_MOBILE = 'mobile'
    
This would render the same type of template for both tablets and mobile devices.


*****
LINKS
*****

Development:
    https://github.com/RevSquare/django-adaptive

Package:
    https://pypi.python.org/pypi/django-adaptive
