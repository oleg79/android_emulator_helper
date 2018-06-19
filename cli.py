import click
import helper
import runner

@click.command()
def cli():
    """
    Android Emulator Device selection CLI.\n
    Just run it and select from available devices.\n
    No option is needed in v0.1.0.
    """
    android_home = helper.get_android_home()
    available_devices = helper.get_emulator_devices()

    selected_device = runner.get_selected_device(available_devices)
    runner.run_selected_device(android_home, selected_device)


if __name__ == '__main__':
    cli()
