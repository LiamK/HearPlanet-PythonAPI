import os
import sys
from ConfigParser import SafeConfigParser, NoOptionError

# Put system wide configuration variables in /etc/hearplanet.cfg.
# Put individual user config in ~/.hearplanet.cfg.
config_files = (
        '%s/hearplanet.cfg' % os.path.dirname(os.path.realpath(__file__)),
        '/etc/hearplanet.cfg',
        os.path.expanduser('~/.hearplanet.cfg'),
        )

parser = SafeConfigParser()
parser.read(config_files)

# HearPlanet server info
HEARPLANET_HOST = parser.get('server', 'HEARPLANET_HOST')
HEARPLANET_PORT = parser.getint('server', 'HEARPLANET_PORT')
EMITTER_FORMAT = parser.get('server', 'EMITTER_FORMAT')
BASE_URL = parser.get('server', 'BASE_URL')
DRIVER_VERSION_TAG = parser.get('server', 'DRIVER_VERSION_TAG')
LOG_LEVEL = parser.get('server', 'LOG_LEVEL')

# Your application credential.
# Application credential is always required.
try:
    APP_CREDENTIALS = {
            'name':parser.get('application_credentials', 'name'),
            'key':parser.get('application_credentials', 'key')
    }
except NoOptionError:
    print 'Misconfiguration? Searched %s for application_credentials "name" and "key"' % str(config_files[1:])
    sys.exit(1)

# Your user credential.
# User credential is optional.
try:
    USER_CREDENTIALS = {
            'name':parser.get('user_credentials', 'name'),
            'key':parser.get('user_credentials', 'key')
    }
except NoOptionError:
    USER_CREDENTIALS = {}
    pass
