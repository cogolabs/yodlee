#!/usr/bin/env python
from setuptools import setup


setup(
    name='yodlee',
    packages=['yodlee'],
    version='0.1.2',
    author='Ben Feeser',
    author_email='bfeeser@cogolabs.com',
    license='Apache 2.0',
    url='https://github.com/cogolabs/yodlee',
    keywords='evestnet yodlee fintech account aggregation',
    install_requires=['requests>=2.13.0'],
    description='Evestnet Yodlee API Client',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ]
)
