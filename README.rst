=========================
Wealthsimple Trade Python
=========================
A convenient Python wrapper for the Wealthsimple Trade API. Note that this wrapper is Unofficial and is not in any way affiliated with Wealthsimple. Please use at your own risk.

.. raw:: html

    <embed>
        <div style="max-height: 50px; max-width: 150px; margin: 0 auto">
        <img src="https://lh3.googleusercontent.com/X-n4zQh48D-J7Vq7sqA7UoJRtMu4uf4Jwh7v3LiI4_-2pmL9PXjwx4r6X5RX4b1Fvpc" width="50px" height="50px">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="50px" height="50px">
        </div>
    </embed>
|
.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/wealthsimple-trade-python/badge/?version=latest
    :target: https://wealthsimple-trade-python.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    
.. |travis| image:: https://api.travis-ci.org/seansullivan44/Wealthsimple-Trade-Python.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/seansullivan44/Wealthsimple-Trade-Python

.. |requires| image:: https://requires.io/github/seansullivan44/Wealthsimple-Trade-Python/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/seansullivan44/Wealthsimple-Trade-Python/requirements/?branch=master

.. |commits-since| image:: https://img.shields.io/pypi/v/wealthsimple-trade-python
    :alt: Commits since latest release
    :target: https://pypi.org/project/wealthsimple-trade-python/

.. end-badges


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

If your Wealthsimple Trade account uses two-factor authentication then you must provide the `WSTrade` object with a callback function as shown in the following example: 
::

    import wealthsimple

    def my_two_factor_function():
        MFACode = ""
        while not MFACode:
            # Obtain user input and ensure it is not empty
            MFACode = input("Enter 2FA code: ")
        return MFACode

    ws = WSTrade(
        "email",
        "password",
        two_factor_callback=my_two_factor_function,
    )
    
Documentation
=============


https://Wealthsimple-Trade-Python.readthedocs.io/

