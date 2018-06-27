import os
import json
import click
import helper
import runner
import settings_manager

@click.command()
@click.option('--default'
             , is_flag=True
             , help='Run default device.')
@click.option('--latest'
             , is_flag=True
             , help='Run latest started device.')
def cli(default=False, latest=False):
    """
Android Emulator Device selection CLI.
Just run it and select from available devices.
    """
    android_home = helper.get_android_home()
    available_devices = helper.get_emulator_devices()

    default_device = settings_manager.get_device_by_status('DefaultDevice')
    latest_started_device = settings_manager.get_device_by_status('LatestStartedDevice')

    if default and default_device in available_devices:
        runner.run_selected_device(android_home, default_device)

    elif latest and latest_started_device in available_devices:
        runner.run_selected_device(android_home, latest_started_device)

    else:
        selected_device = runner.get_selected_device(available_devices)

        runner.run_selected_device(android_home, selected_device)

if __name__ == '__main__':
    cli()
