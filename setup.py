#!/usr/bin/env python

from setuptools import setup

setup(
    name='libfaketimefs-controller',
    version='0.0.1',
    description='Control libfaketimefs',
    author='Raymond Butcher',
    author_email='ray.butcher@claranet.uk',
    url='https://github.com/claranet/libfaketimefs-controller',
    license='MIT License',
    packages=(
        'libfaketimefs_controller',
    ),
    scripts=(
        'bin/libfaketimefs-ctl',
    ),
)
