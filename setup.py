#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='django-adaptive',
    version='1.0.0',
    author='Guillaume Pousseo <guillaumepousseo@revsquare.com>,\
        Tomasz Roszko <tomaszroszko@revsquare.com>,\
        Rafal Selewonko <rafalselewonko@revsquare.com>',
    description='Manages to load templates according to the type of device to\
        a specific directory prefix.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'Django>=1.6',
        'django-mobi>=0.1.7',
    ],
)
