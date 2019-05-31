setup_python_package
======================================================================
|travis| |pip|

A python package that helps you create a python package.

The script will guide you step by step in creating the python package and integrating it with sonarcloud, travis and coveralls.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install setup_python_package

Requirements
----------------------------------------------
You will need to have install the travis gem for encryption:

.. code:: shell

    gem install travis

Usage example
-----------------------------------------------
Open a python shell in your repository and import the package, in the usual fashion:

.. code:: python

    from setup_python_package image setup_python_package
    setup_python_package()

The just follow the istructions, that go something like this (this is taken directly from the setup of another repo o' mine):

.. code:: bash

    Please insert package name [dict_hash]: 
    Please insert author name [Luca Cappelletti]: 
    Please insert author email [cappelletti.luca94@my.email.com]: 
    Please insert package url [https://github.com/LucaCappelletti94/dict_hash]: 
    Please insert package description [Simple python tool to hash dictionaries using both default hash and sha256.]: Please insert package version [1.0.0]: 
    Please insert tests directory [tests]: 
    You might need to create the travis project.
    Press any key to go to travis now.
    You might need to create the sonarcloud project.
    Just copy the project key and paste it here.
    Press any key to go to sonar now.
    Please insert sonar project key: (sonar key goes here, removed for privacy)
    Please run the following into a terminal window in this repository:
    travis encrypt (sonar key goes here, removed for privacy)
    Copy only the generate key here, it looks like this:
    secure: "very_long_key" 
    Please insert travis project key: (travis key goes here, removed for privacy)
    Please insert python version [3.7]: 
    You still need to create the coveralls project.
    Just copy the repo_token and paste it here.
    Press any key to go to coveralls now.


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/setup_python_package.png
   :target: https://travis-ci.org/LucaCappelletti94/setup_python_package

.. |pip| image:: https://badge.fury.io/py/setup_python_package.svg
    :target: https://badge.fury.io/py/setup_python_package


