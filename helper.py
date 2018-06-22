import os
import sys
import subprocess
from click import ClickException


def get_android_home():
    """
    Retrives $ANDROID_HOME env variable.
    """
    android_home = os.environ.get('ANDROID_HOME')
    if android_home is None:
        raise ClickException('''
$ANDROID_HOME is not found.
Please be sure that $ANDROID_HOME enviroment variable has been exported.
        ''')

    return android_home


def get_emulator_devices():
    """
    Retrives a list of available emulator devices.
    """
    cmd = ['emulator', '-list-avds']

    if sys.version_info.major == 3:
        result = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    else:
        result = subprocess.check_output(cmd)

    
    devices = result.strip().split('\n')

    if len(devices) == 0:
        raise RuntimeError('No available emulator diviceswere found.')

    return devices

    
    