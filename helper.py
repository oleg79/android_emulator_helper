import os
import sys
import subprocess
import click


def get_android_home():
    """
    Retrives $ANDROID_HOME env variable.
    """
    android_home = os.environ.get('ANDROID_HOME')
    if android_home is None:
        click.secho('$ANDROID_HOME environment variable is not found', fg='red')
        value = click.prompt('Please specify android sdk path manualy for the current session', type=str)

        if os.path.isdir(value):
            return value
        else:
            raise click.ClickException("""
$ANDROID_HOME is not found.
Please be sure that $ANDROID_HOME enviroment variable has been exported.
            """)

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
        raise click.ClickException('No available emulator diviceswere found.')

    return devices

    
    