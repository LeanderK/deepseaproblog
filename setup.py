from setuptools import setup

setup(
    name='DeepSeaProbLog',
    version='1.0',
    packages=['deepsea', 'deepsea.examples', 'deepsea.engines', 'deepsea.semiring', 'deepsea.utils'],
    package_dir={
        'deepsea': '.',
        'deepsea.examples': './examples',
        'deepsea.engines': './engines',
        'deepsea.semiring': './semiring',
        'deepsea.utils': './utils',
    },
    author='Lennert De Smet, Pedro Zuidberg Dos Martires, Robin Manhaeve, Giuseppe Marra, Angelika Kimmig, Luc De Raedt',
    license_files = ('LICENSE',),
)