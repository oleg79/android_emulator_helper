import json
import subprocess
from pick import Picker
import settings_manager

def set_default_device(picker):
    """
    Calls set default device logic.
    """
    option, _ = picker.get_selected()
    settings_manager.set_device_status(option, 'DefaultDevice')
    return None

def get_selected_device(devices):
    """
    Prints available devices as selectable option list.
    Returns selected option.
    """
    picker = Picker(devices, 'Select device:', options_map_func=settings_manager.map_device_status)

    picker.register_custom_handler(ord('s'), set_default_device)

    option, _ = picker.start()
    return option


def run_selected_device(android_home, device_name):
    """
    Runs selected device.
    """
    cmd = [
        "{}/emulator/emulator".format(android_home),
        "@{}".format(device_name)
    ]
    settings_manager.set_device_status(device_name, 'LatestStartedDevice')
    subprocess.run(cmd)