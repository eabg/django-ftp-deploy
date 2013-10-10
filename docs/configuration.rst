Configuring django-ftp-deploy
=============================

Configuration django-ftp-deploy module

Django Project
--------------

* Add configuration to your settings::

    DEPLOY_SECRET_KEY = ''

    DEPLOY_BITBUCKET_SETTINGS = {
        'username'      : '',
        'password'      : '',
        'branch'        : '',
    }

    DEPLOY_FTP_SETTINGS = {
        'host'      : '',
        'username'  : '',
        'password'  : '',
        'path'      : '',
    }


  ``DEPLOY_SECRET_KEY``
        unique deploy key for your django project


  ``DEPLOY_BITBUCKET_SETTINGS``
        | *username*: username to your bitbucket account
        | *password*: password to your bitbucket account
        | *branch*: deployed GIT branch


  ``DEPLOY_FTP_SETTINGS``
        | *host*: host of your FTP server
        | *username*: username to your FTP server
        | *password*: password to your FTP server
        | *path*: absolute path to root folder of your project
       

Bitbucket Repository
--------------------

* Add POST hook to your repository::

    http://www.yourdomain.pl/ftpdeploy/bitbucket/DEPLOY_SECRET_KEY


