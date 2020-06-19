========
Overview
======== 
.. raw:: html

    <embed>
        <div style="max-height: 50px; max-width: 150px;">
        <img src="https://lh3.googleusercontent.com/X-n4zQh48D-J7Vq7sqA7UoJRtMu4uf4Jwh7v3LiI4_-2pmL9PXjwx4r6X5RX4b1Fvpc" width="50px" height="50px">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="50px" height="50px">
        </div>
    </embed>
    
.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/Wealthsimple-Trade-Python/badge/?style=flat
    :target: https://readthedocs.org/projects/Wealthsimple-Trade-Python
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/seansullivan44/Wealthsimple-Trade-Python.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/seansullivan44/Wealthsimple-Trade-Python

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/seansullivan44/Wealthsimple-Trade-Python?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/seansullivan44/Wealthsimple-Trade-Python

.. |requires| image:: https://requires.io/github/seansullivan44/Wealthsimple-Trade-Python/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/seansullivan44/Wealthsimple-Trade-Python/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/seansullivan44/Wealthsimple-Trade-Python/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/seansullivan44/Wealthsimple-Trade-Python

.. |commits-since| image:: https://img.shields.io/github/commits-since/seansullivan44/Wealthsimple-Trade-Python/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/seansullivan44/Wealthsimple-Trade-Python/compare/v0.0.1...master



.. end-badges

A convenient Python wrapper for the Wealthsimple Trade API. Note that this wrapper is Unofficial and is not in any way affiliated with Wealthsimple. Please use at your own risk.


Installation
============

::

    pip install wealthsimple-trade-python

You can also install the in-development version with::

    pip install https://github.com/seansullivan44/Wealthsimple-Trade-Python/archive/master.zip

Getting Started
===============
Download the Wealthsimple Trade app for iOS or Android and create an account. This API wrapper will use your Wealthsimple Trade login credentials to make successful API calls. After creating an account, use your login credentials to create a WSTrade object:
::

    import wealthsimple
    WS = wealthsimple.WSTrade('email', 'password')

Documentation
=============


https://Wealthsimple-Trade-Python.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
