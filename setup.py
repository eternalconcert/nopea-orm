# coding: utf-8
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setupargs = {
    'name': 'nopea',
    'description': 'Provides a simple ORM for MySQL and SQLite.',

    'license': 'GPLv3',
    'version': '0.0.2',

    'packages': ['nopea', 'nopea.adaptors'],
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',

    'author': 'Christian Kokoska',
    'author_email': 'info@softcreate.de',
    'install_requires': [
        'colorama==0.3.9',
        'ipython==6.4.0'
    ],
}

if __name__ == '__main__':
    setup(**setupargs)
