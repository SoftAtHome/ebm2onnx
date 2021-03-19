#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'onnx>=1.8',
    'interpret-core>=0.2',
 ]

setup(
    author="Romain Picard",
    author_email='romain.picard@softathome.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="EBM model serialization to ONNX",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ebm2onnx',
    name='ebm2onnx',
    packages=find_packages(include=['ebm2onnx']),
    setup_requires=setup_requirements,
    url='https://github.com/SoftAtHome/ebm2onnx.git',
    version='0.0.0',
    zip_safe=True,
)
