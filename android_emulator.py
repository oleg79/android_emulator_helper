import os
import json
import click
import helper
import runner
import settings_manager

@click.command()
def cli():
    """
Android Emulator Device selection CLI.
Just run it and select from available devices.
No option is needed in v0.1.0.
    """
    android_home = helper.get_android_home()
    available_devices = helper.get_emulator_devices()

    click.echo('asim-select CLI. Developed by Oleg Kapustin.') 

    selected_device = runner.get_selected_device(available_devices)

    settings_manager.set_device_status(selected_device, 'LatestStartedDevice')

    runner.run_selected_device(android_home, selected_device)


if __name__ == '__main__':
    cli()
