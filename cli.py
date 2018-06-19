import os
import subprocess
import click
from pick import pick

@click.command()
def cli():
    android_home = get_android_home()
    device_name = get_selected_device(get_emulator_devices())
    run_selected_device(android_home, device_name)

def get_android_home():
    android_home = os.environ.get('ANDROID_HOME')
    if android_home == None:
        raise RuntimeError('$ANDROID_HOME not found.')
    return android_home

def get_emulator_devices():
    cmd = ['emulator', '-list-avds']
    result = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return result.strip().split('\n')

def get_selected_device(devices):
    title = 'Select device:'
    option, _ = pick(devices, title)
    return option

def run_selected_device(android_home, device_name):
    cmd = [
        "{}/emulator/emulator".format(android_home),
        "@{}".format(device_name)
    ]
    subprocess.run(cmd)


if __name__ == '__main__':
    cli()
