# coding: utf-8
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setupargs = {
    'name': 'nopea',
    'description': 'Provides a simple ORM for MySQL, PostgreSQL and SQLite.',

    'license': 'GPLv3',
    'version': '0.5.1',

    'packages': ['nopea', 'nopea.adaptors'],
    'long_description': long_description,
    'long_description_content_type': 'text/x-rst',

    'author': 'Christian Kokoska',
    'author_email': 'christian@eternalconcert.de',
    'install_requires': [
        'mysqlclient==1.3.10',
        'colorama==0.3.9',
        'ipython==6.4.0'
    ],
}

if __name__ == '__main__':
    setup(**setupargs)
