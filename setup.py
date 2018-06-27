import setuptools
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


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='asim-select',
    version='0.2.0',
    author='Oleg Kapustin',
    author_email='0112oleg@gmail.com',
    description='''
        A simple CLI to run android emulator devices\n
        without starting Android Studio.
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/oleg79/android_emulator_helper',
    packages=setuptools.find_packages(),
    py_modules=[
        'android_emulator',
        'helper',
        'runner',
        'settings_manager',
    ],
    keywords='android emulator cli',
    license='MIT',
    install_requires=[
        'Click',
        'pick',
    ],
    entry_points='''
        [console_scripts]
        asim-select=android_emulator:cli
    ''',
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand,
    },
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
