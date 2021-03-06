setup_python_package
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip|

A python package that helps you create a python package.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install setup_python_package

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get
slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Requirements
----------------------------------------------
You will need to have install the travis gem for encryption:

.. code:: shell

    gem install travis

Usage example
-----------------------------------------------
In your terminal, from within a valid repository, just run the following:

.. code:: bash

    spp

The just follow the istructions, that go something like this
(this is taken directly from the setup of another repo o' mine):

.. code:: bash

    Please insert package name [dict_hash]: 
    Please insert author name [Luca Cappelletti]: 
    Please insert author email [cappelletti.luca94@my.email.com]: 
    Please insert package url [https://github.com/LucaCappelletti94/dict_hash]: 
    Please insert package description [Simple python tool to hash dictionaries using both default hash and sha256.]: Please insert package version [1.0.0]: 
    Please insert tests directory [tests]: 
    You might need to create the travis project.
    Press enter to go to travis now.
    You might need to create the sonarcloud project.
    Just copy the project key and paste it here.
    Press enter to go to sonar now.
    Please insert sonar project key: (sonar key goes here, removed for privacy)
    Please run the following into a terminal window in this repository:
    travis encrypt (sonar key goes here, removed for privacy)
    Copy only the generate key here, it looks like this:
    secure: "very_long_key" 
    Please insert travis project key: (travis key goes here, removed for privacy)
    Please insert python version [3.7]: 
    You still need to create the coveralls project.
    Just copy the repo_token and paste it here.
    Press enter to go to coveralls now.

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/setup_python_package.png
   :target: https://travis-ci.org/LucaCappelletti94/setup_python_package
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_setup_python_package&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_setup_python_package
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_setup_python_package&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_setup_python_package
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_setup_python_package&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_setup_python_package
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/setup_python_package/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/setup_python_package?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/setup-python-package.svg
    :target: https://badge.fury.io/py/setup-python-package
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/setup-python-package
    :target: https://pepy.tech/badge/setup-python-package
    :alt: Pypi total project downloads

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/bc8592ec13494b30b87da0af3170defb
    :target: https://www.codacy.com/app/LucaCappelletti94/setup_python_package?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/setup_python_package&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/8fcc0685ff43463f2b44/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/setup_python_package/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/8fcc0685ff43463f2b44/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/setup_python_package/test_coverage
    :alt: Code Climate Coverate
