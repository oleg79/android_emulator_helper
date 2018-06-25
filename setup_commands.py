from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

def create_json():
    with open('./data.json','w') as datafile:
        datafile.write('{}')


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        create_json()


class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        create_json()


class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        create_json()
