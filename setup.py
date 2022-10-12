from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='complice-api',
    version='0.1.0',
    author='Complice',
    author_email='team@complice.co',
    description='A Python wrapper for the Complice API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/complice/complice-api-python',
    packages=['complice'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
