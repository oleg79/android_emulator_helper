import sys
import click

def get_selected_device(devices):
    curr = 0
    selected = None
    for index, device in enumerate(devices):
        click.secho('* ' if index == curr else '  ', fg='cyan', nl=False)
        click.secho(device, fg=('cyan' if index == curr else 'white'))
    selected = sys.stdin.read(1)
    click.echo(selected)