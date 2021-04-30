import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.MD')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-firebase',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Django firebase support.',
    long_description=README,
    url='',
    author='Grigory Leikin (reOiL)',
    author_email='imidg3001@yandex.ru',
    zip_safe=False,
    license='BSD 3-Clause License',
    platforms=['any'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django ::2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=2.0',
        'firebase-admin>=5.0.0'
    ],
)