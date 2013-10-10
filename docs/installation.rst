Installing django-ftp-deploy
============================

Installation and requirements for django-ftp-deploy module

Installation
------------

#. `Download <https://pypi.python.org/pypi/django-ftp-deploy/>`_  and install ``django-ftp-deploy`` with `requirements`_ manually,
    
   or Install ``django-ftp-deploy`` using pip::

        pip install django-ftp-deploy


#. Add ``ftp_deploy`` to your ``INSTALLED_APPS`` list in your settings
   
   .. code-block:: python

    INSTALLED_APPS = (
      ...
      'ftp_deploy',
      ...
    )    

#. Add ``django-ftp-deploy`` to your ``urlpatterns`` list in your urls

   .. code-block:: python

        urlpatterns = patterns('',
            ...
            url(r'^ftpdeploy/', include('ftp_deploy.urls')),
            ...
          )


Requirements
------------   

Required third party libraries are **installed automatically** if you use pip to install django-ftp-deploy

1. `pycurl <https://pypi.python.org/pypi/pycurl>`_
2. `certifi <https://pypi.python.org/pypi/certifi>`_