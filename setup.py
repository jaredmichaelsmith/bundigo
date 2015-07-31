# -*- coding: utf-8 -*-


import re
from distutils.core import setup


version = re.search(
    '^__version__\s*=\*"(.*)"',
    open('bundigo/bundigo.py').read(),
    re.M
    ).group(1)


with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')


setup(
    name = 'bundigo',
    packages = ['bundigo'],
    entry_points = {
        'console_scripts': ['bundigo = bundigo.bundigo.main']
        },
    version = version,
    description = "Your one-stop shop for starting a software project",
    long_description = long_descr,
    license = 'MIT',
    author = 'Jared Smith',
    author_email = 'jared@jaredsmith.io',
    url = 'https://jaredmichaelsmith.com/bundigo',
    install_requires=[
    ],
)
