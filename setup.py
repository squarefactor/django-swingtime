#!/usr/bin/env python
from distutils.core import setup


VERSION = '1.0' 

README_FILE = open('README')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

 
setup(
    name='django-swingtime',
    version=VERSION,
    url='http://github.com/squarefactor/django-swingtime.git',
    description='Swingtime is a Django calendar application.',
    long_description=long_description,
    author='David A Krauth',
    platforms=['any'],
    packages=[
        'swingtime',
        'swingtime.conf'
    ],
)
