from setuptools import setup

setup(
    name='asim-select',
    version='0.1.0',
    author='Oleg Kapustin',
    author_email='0112oleg@gmail.com',
    description='''
        A simple CLI to run android emulator devices\n
        without starting Android Studio.
    ''',
    py_modules=['android_emulator'],
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
)
