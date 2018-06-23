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

def map_device_status(option):
    """
    Maps options with their statuses if such exits for options list display.
    """
    stats = []

    with open('data.json', 'r') as datafile:
        data = json.load(datafile)
    if option == data.get('DefaultDevice', False):
        stats.append('default')
    if option == data.get('LatestStartedDevice', False):
        stats.append('latest started')

    return "{} {}".format(option, ", ".join(stats))

