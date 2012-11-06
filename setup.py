#from distutils.core import setup
import multiprocessing, logging
from setuptools import setup, find_packages

setup(
    name = 'HearPlanetAPI',
    version = '0.1.0',
    description = 'HearPlanet API driver',
    long_description = open('README.rst').read(),
    keywords = 'HearPlanet API driver',
    url = 'http://pypi.python.org/pypi/HearPlanetAPI/',
    license = 'LICENSE.txt',
    author = 'Liam Kirsher',
    author_email = 'liam@hearplanet.com',
    zip_safe = True,

    packages = find_packages(exclude=['tests', 'examples']),
    include_package_data = True,
    data_files = [('/etc/', ['cfg/hearplanet.cfg'])],
    install_requires = [ 'requests', ],

    tests_require = ['nose'],
    test_suite = 'nose.collector',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
