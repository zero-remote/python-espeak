#! /usr/bin/env python

from setuptools import setup, Extension, Command

module = Extension('espeak.core',
	sources = ['espeak/espeakmodulecore.cpp'],
	libraries = ['espeak-ng'],
    include_dirs = ['/usr/include/python3.5m'],
    library_dirs=['/usr/local/lib'])

setup(
    name = 'pySpeak',
    version = '0.1',
    description = 'Python C extension for the eSpeak speech synthesizer',
    author = 'Swapnil Davangave',
    author_email = 'swapnil.davangave@liveweaver.com',
    url = 'https://github.com/zero-remote/python-espeak',
    license = 'GNU GPL',
    platforms = 'posix',
    ext_modules = [module],
    packages = ['espeak'],
    long_description = open("README.rst").read(),
    )
