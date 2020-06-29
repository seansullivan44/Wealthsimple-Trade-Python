#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

"""
def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()
"""

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="wealthsimple-trade-python",
    version="1.0.5",
    license="MIT",
    description="Python wrapper for the Wealthsimple Trade API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Sean Sullivan",
    author_email="sean.mc.sullivan@gmail.com",
    url="https://github.com/seansullivan44/Wealthsimple-Trade-Python",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://Wealthsimple-Trade-Python.readthedocs.io/",
        "Changelog": "https://Wealthsimple-Trade-Python.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/seansullivan44/Wealthsimple-Trade-Python/issues",
    },
    keywords=["wealthsimple", "trade", "finance", "stocks", "market", "api", "wrapper"],
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["requests",],
)
