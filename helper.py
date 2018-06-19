import os
import subprocess


def get_android_home():
    """
    Retrives $ANDROID_HOME env variable.
    """
    android_home = os.environ.get('ANDROID_HOME')
    if android_home is None:
        raise RuntimeError('$ANDROID_HOME not found.')

    return android_home


def get_emulator_devices():
    """
    Retrives a list of available emulator devices.
    """
    cmd = ['emulator', '-list-avds']
    result = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    devices = result.strip().split('\n')

    if len(devices) == 0:
        raise RuntimeError('No available emulator diviceswere found.')

    return devices

    
    