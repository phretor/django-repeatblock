import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-repeatblock',
    version = '0.1',
    description = 'A template tag that allows to repeat template blocks'\
        ' within the same template file.',
    long_description = read('README.rst'),
    
    author  ='Federico Maggi',
    author_email = 'federico@maggi.cc',
    url = 'http://github.com/phretor/django-repeatblock',
    
    packages = find_packages(exclude=['example']),
    zip_safe = False,
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    
    install_requires = ['setuptools', 'Django >= 1.3'],
)
