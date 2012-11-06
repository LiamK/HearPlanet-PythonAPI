from distutils.core import setup

setup(
    name='HearPlanetAPI',
    version='0.1.0',
    author='Liam Kirsher',
    author_email='liam@hearplanet.com',
    packages=['hearplanet', 'hearplanet.test', 'hearplanet.query'],
    scripts=['scripts/example.py'],
    data_files=[('/etc/', ['cfg/hearplanet.cfg'])],
    url='http://pypi.python.org/pypi/HearPlanetAPI/',
    license='LICENSE.txt',
    description='.',
    long_description=open('README.txt').read(),
    requires=[
        'requests',
    ],
)
