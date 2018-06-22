import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='asim-select',
    version='0.0.4',
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
    py_modules=['android_emulator', 'helper', 'runner'],
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
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
