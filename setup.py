"""
Python scripts
"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='testing',
    version='0.1.0',
    license='UNLICENSED',
    packages=find_packages(
        include=[
            'testing',
            'testing.basic.*'
        ]
    ),
    install_requires=[
        'argparse',
        'click'
    ]
)
