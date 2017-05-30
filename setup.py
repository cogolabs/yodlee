from setuptools import setup


setup(
    name='yodlee',
    packages=['yodlee'],
    version='0.1.6',
    author='Ben Feeser',
    author_email='bfeeser@cogolabs.com',
    license='Apache 2.0',
    url='https://github.com/cogolabs/yodlee',
    keywords='envestnet yodlee fintech account aggregation',
    install_requires=['requests'],
    description='Envestnet Yodlee API Client',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
