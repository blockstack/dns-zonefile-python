#!/usr/bin/env python
"""
DNS Zone File
==============

"""

from setuptools import setup, find_packages

setup(
    name='blockstack-zones-py3',
    version='0.19.0.0',
    url='https://github.com/jaywink/zone-file-py',
    license='MIT',
    author='Blockstack Developers',
    author_email='hello@onename.com',
    maintainer='Jason Robinson',
    maintainer_email='mail@jasonrobinson.me',
    description="Library for creating and parsing DNS zone files",
    keywords='dns zone file zonefile parse create',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
