import os
from . import thermostat
from . import thermometer
from . import envcontroller
from . import output
from . import apps

def _get_config_file_location():
    """
    Locate a Braubuddy config file
    """
    return os.path.join(CONFIG_DIR, CONFIG_FILENAME_BRAUBUDDY)

# Base dirs
THIS_DIR = os.path.join(os.getcwd(), 'braubuddy')
CONFIG_DIR = os.path.join(THIS_DIR, 'config')
TEMPLATE_DIR = os.path.join(THIS_DIR, 'templates')
# Internal config files
CONFIG_FILE_DASHBOARD = os.path.join(CONFIG_DIR, 'dashboard')
CONFIG_FILE_API = os.path.join(CONFIG_DIR, 'api')
# User config file
CONFIG_FILENAME_BRAUBUDDY = 'braubuddy'
CONFIG_FILE_BRAUBUDDY = _get_config_file_location()
# Recent state data
RECENT_DATA = output.ListMemoryOutput()
