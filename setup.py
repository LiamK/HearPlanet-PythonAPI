import multiprocessing, logging
from setuptools import setup, find_packages

setup(
    name = 'HearPlanetAPI',
    version = '0.1.0',
    description = 'HearPlanet API driver',
    long_description = open('README.rst').read(),
    keywords = 'HearPlanet API driver',
    url = 'http://pypi.python.org/pypi/HearPlanetAPI/',
    author = 'Liam Kirsher',
    author_email = 'liam@hearplanet.com',
    zip_safe = True,

    packages = find_packages(exclude=['tests', 'examples']),
    include_package_data = True,
    exclude_package_data = {'': ['.gitignore']}, 
    data_files = [('/etc/', ['cfg/hearplanet.cfg'])],
    install_requires = [ 'requests', ],
    setup_requires = [ 'setuptools_git >= 0.3', ],

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
