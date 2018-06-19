import subprocess
from pick import pick

def get_selected_device(devices):
    """
    Print available devices as selectable option list.
    Returns selected option.
    """
    title = 'Select device:'
    option, _ = pick(devices, title)
    return option


def run_selected_device(android_home, device_name):
    """
    Runs selected device.
    """
    cmd = [
        "{}/emulator/emulator".format(android_home),
        "@{}".format(device_name)
    ]
    subprocess.run(cmd)