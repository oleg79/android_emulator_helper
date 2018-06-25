import os
import json

def set_device_status(device_name, key):
    """
    Saves device status to data.json.
    """
    with open('data.json', 'r') as datafile:
        data = json.load(datafile)

    with open('data.json', 'w+') as datafile:
        data[key] = device_name
        json.dump(data, datafile)

def get_device_by_status(status):
    """
    Returns device name by status.
    """
    with open('data.json', 'r') as datafile:
        data = json.load(datafile)
    return data.get(status, None)

def map_device_status(option):
    """
    Maps options with their statuses if such exits for options list display.
    """
    stats = []

    if option == get_device_by_status('DefaultDevice'):
        stats.append('default')
    if option == get_device_by_status('LatestStartedDevice'):
        stats.append('latest started')

    return "{} {}".format(option, ", ".join(stats))

