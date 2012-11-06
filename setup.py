from distutils.core import setup

setup(
    name='HearPlanetAPI',
    version='0.1.0',
    author='Liam Kirsher',
    author_email='liam@hearplanet.com',
    packages=['hearplanet', 'hearplanet.test', 'hearplanet.query'],
    package_data={'':['*.cfg']},
    data_files=[('/etc/', ['cfg/hearplanet.cfg'])],
    url='http://pypi.python.org/pypi/HearPlanetAPI/',
    license='LICENSE.txt',
    description='HearPlanet API driver',
    long_description=open('README').read(),
    requires=[
        'requests',
    ],
)
