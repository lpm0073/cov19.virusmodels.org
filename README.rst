cov19.virusmodels.org
=====================
.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

.. image:: https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg
     :target: https://lawrencemcdaniel.com
     :alt: Hack.d Lawrence McDaniel

:License: MIT

A community-supported Django/React web platform to host growth models and decision-support models for 
Viruses and other pandemics.

-  `GitHub Repository <https://github.com/lpm0073/cov19.virusmodels.org>`__


Development Environment Setup
-----------------------------
The dev environment depends on postgres in your local dev environment, so make sure that you have this.
It MIGHT be handled with the projects requirements/local.txt (i have not checked) -- please advise if you know.

* (lawrence) I am setting up .env for the project so that we can get CI working this morning. be aware you might 
need to "git checkout" often today as i get this working.

For additional help refer to: https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html

Dependencies
^^^^^^^^^^^^

-  Python 3.4, 3.5 or 3.6
-  `Virtualenv <https://virtualenv.pypa.io/en/stable/installation/>`__
-  `VirtualenvWrapper <https://virtualenvwrapper.readthedocs.io/en/latest/install.html>`__
   (optional)

Setup
^^^^^

1. Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then activate it and install all pip
requirements. Also, run migrations, load initial data (if any), and
start the dev web server to ensure that the site comes up:

.. code:: bash

    $ git clone https://github.com/lpm0073/cov19.virusmodels.org.git
    $ cd cov19.virusmodels.org
    $ python3.7 -m venv venv
    $ source venv/bin/activate

2. Install Python requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash


    $ pip install --upgrade pip
    $ pip install -r cov19/requirements/local.txt



3. Create a new PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If this is your first time to use PostgreSQL on your local computer then you'll need to 
download and install it: https://www.postgresql.org/

.. code:: bash

    $ createdb cov19 -U postgres --password cov19

4. Set environment variables for postgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
edit cov19/config/settings/base.py, replacing this code 

.. code:: python

    DATABASES = {
        "default": env.db("DATABASE_URL", default="postgres:///cov19")
    }

with the following:

.. code:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cov19',
            'USER': 'YOUR-POSTGRESQL-USERNAME-GOES-HERE',
            'PASSWORD': 'YOUR-POSTGRESQL-PASSWORD-GOES-HERE',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


5. Create a new file: cov19/.env
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add the following row to this file and then save:

.. code:: python

    CELERY_BROKER_URL = "amqp://"


6. Bootstrap Django locally 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ cov19/manage.py migrate

    $ # results should aproximaely like the following ....
    $ Operations to perform:
    $ Apply all migrations: account, admin, auth, contenttypes, sessions, sites, socialaccount, users
    $ Running migrations:
    $ Applying contenttypes.0001_initial... OK
    $ Applying contenttypes.0002_remove_content_type_name... OK
    $ Applying auth.0001_initial... OK
    $ Applying auth.0002_alter_permission_name_max_length... OK
    $ Applying auth.0003_alter_user_email_max_length... OK
    $ Applying auth.0004_alter_user_username_opts... OK
    $ Applying auth.0005_alter_user_last_login_null... OK
    $ Applying auth.0006_require_contenttypes_0002... OK
    $ Applying auth.0007_alter_validators_add_error_messages... OK
    $ Applying auth.0008_alter_user_username_max_length... OK
    $ Applying users.0001_initial... OK
    $ ...
    $ ...
    $ Applying django_celery_beat.0002_auto_20161118_0346... OK
    $ Applying django_celery_beat.0003_auto_20161209_0049... OK
    $ Applying django_celery_beat.0004_auto_20170221_0000... OK
    $ Applying django_celery_beat.0005_add_solarschedule_events_choices... OK
    $ Applying django_celery_beat.0006_auto_20180322_0932... OK
    $ Applying django_celery_beat.0007_auto_20180521_0826... OK
    $ Applying django_celery_beat.0008_auto_20180914_1922... OK
    $ Applying django_celery_beat.0006_auto_20180210_1226... OK
    $ Applying django_celery_beat.0006_periodictask_priority... OK
    $ Applying django_celery_beat.0009_periodictask_headers... OK
    $ Applying django_celery_beat.0010_auto_20190429_0326... OK
    $ Applying django_celery_beat.0011_auto_20190508_0153... OK
    $ Applying django_celery_beat.0012_periodictask_expire_seconds... OK


7. Create a Django superuser 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ cov19/manage.py createsuperuser


8. Launch the site from your local web server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ cov19/manage.py runserver

    $ # results should look approximately like the following ....
    $ Watching for file changes with StatReloader
    $ INFO 2020-03-14 18:31:18,058 autoreload 68771 4622261696 Watching for file changes with StatReloader
    $ Performing system checks...
    $ 
    $ System check identified no issues (0 silenced).
    $ March 14, 2020 - 18:31:18
    $ Django version 2.2.11, using settings 'config.settings.local'
    $ Starting development server at http://127.0.0.1:8000/
    $ Quit the server with CONTROL-C.


Cookiecutter Settings
---------------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy cov19

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html


Celery
------

This app uses Celery and RabbitMQ.

To run a celery worker:

.. code-block:: bash

    cd cov19
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. 
If you are in the same folder with *manage.py*, you should be right.


Production Environment Setup
----------------------------
Deployment to Ubuntu 18.04 LTS

-  Ubuntu configuration
-  SSH configuration
-  MySql Installation
-  Python Django Installation
-  Python Django Configuration
-  Gunicorn Configuration
-  Nginx Installation & configuration

Ubuntu configuration
^^^^^^^^^^^^^^^^^^^^

::

    sudo apt-get update
    sudo apt-get install nginx mysql-server python3-pip python3-dev libmysqlclient-dev ufw python3-venv curl libpq-dev


MySql Installation
^^^^^^^^^^^^^^^^^^

::

    # contact Lawrence McDaniel lpm0073@gmail.com if you 
    # need MySQL root access.

    $ mysql -u root -h wordpress-sql.cp6gb73qx6d7.us-west-2.rds.amazonaws.com -p
    mysql> CREATE DATABASE cov19 CHARACTER SET 'utf8';
    mysql> CREATE USER cov19;
    mysql> GRANT ALL ON cov19.* TO 'cov19'@'%' IDENTIFIED BY 'cov19';
    mysql> FLUSH PRIVILEGES;
    mysql> quit

**Note: if you are rebuilding the production environment from scratch
(god help you) then you'll need to use these command to re-initialize
the database from scratch:**

::

    find . -name `'*.pyc'` | xargs rm -r

    sudo rm -r /home/ubuntu/cov19.virusmodels.org/cov19/base/migrations
    sudo rm -r /home/ubuntu/cov19.virusmodels.org/cov19/blog/migrations
    sudo rm -r /home/ubuntu/cov19.virusmodels.org/cov19/breads/migrations
    sudo rm -r /home/ubuntu/cov19.virusmodels.org/cov19/locations/migrations
    sudo rm -r /home/ubuntu/cov19.virusmodels.org/cov19/users/migrations

    ./manage.py makemigrations

Python Django Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # first time installation
    cd ~
    sudo rm -r ./cov19.virusmodels.org
    git clone https://github.com/lpm0073/cov19.virusmodels.org.git

    python3 -m venv ~/cov19.virusmodels.org/venv
    source ~/cov19.virusmodels.org/venv/bin/activate
    pip install -r ~/cov19.virusmodels.org/cov19/requirements/production.txt


    # for CI 
    cd ~/cov19.virusmodels.org
    git checkout . 
    git pull


Ensure that settings.production.py credentials match whatever you used
in the MySql installation above:

::

    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'OPTIONS': {
                 'sql_mode': 'traditional',
             },
             'NAME': 'cov19',
             'USER': 'cov19',
             'PASSWORD': 'cov19',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }

Ensure that settings.production.py for STATIC\_URL AND MEDIA\_URL are
consistent with file locations on the server:

::

    # directories for static files
    STATIC_URL='/static/'
    STATIC_ROOT=os.path.join(BASE_DIR, 'static/')
    MEDIA_URL='/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

Python Django Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a ~/cov19.virusmodels.org/.env file

::

    vim ~/cov19.virusmodels.org/.env
    DJANGO_SETTINGS_MODULE = cov19.config.settings.production
    DJANGO_SECRET_KEY = 'A STRONG KEY THAT IS USED BY DJANGO.'


Add a cov19.virusmodels.org/cov19/settings/secrets.py file with values
for

::


    DATABASES_PASSWORD = 'YOUR TOP-SECRET PASSWORD'

Initiate the Django build sequence to initialize the database, load
Wagtail sample data, compile static assets and finally, test the build
by starting the development web server. If there are no errors generated
from the web server launch then the built might have been successful.

::

    $ cd ~/cov19.virusmodels.org
    $ source ~/cov19.virusmodels.org/venv/bin/activate
    (env) $ python cov19/manage.py makemigrations
    (env) $ python cov19/manage.py migrate
    (env) $ python cov19/manage.py collectstatic
    (env) $ python cov19/manage.py runserver

Gunicorn Configuration
^^^^^^^^^^^^^^^^^^^^^^

Test to see if gunicorn starts correctly:

::

    $ cd ~/cov19.virusmodels.org
    $ source ~/cov19.virusmodels.org/venv/bin/activate
    (env) $ cd ~/cov19.virusmodels.org/
    (env) $ gunicorn --bind 0.0.0.0:8000 cov19.wsgi:application
    (env) $ deactivate

Link gunicorn configuration socket and service files:

::

    $ sudo ln -s /home/ubuntu/cov19.virusmodels.org/etc/systemd/system/gunicorn.socket /etc/systemd/system/
    $ sudo ln -s /home/ubuntu/cov19.virusmodels.org/etc/systemd/system/gunicorn.service /etc/systemd/system/

Enable Gunicorn service at startup:

::

    $ sudo systemctl enable gunicorn.socket
    $ sudo systemctl start gunicorn.socket
    $ sudo systemctl status gunicorn.socket
    $ sudo journalctl -u gunicorn.socket

Check to ensure that the gunicorn socket exists:

::

    $ file /run/gunicorn.sock

Trouble shooting aids:

::

    $ sudo systemctl status gunicorn
    $ sudo systemctl daemon-reload
    $ sudo systemctl restart gunicorn
    $ sudo systemctl stop gunicorn

Nginx Installation & configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ # add the nginx config file from this repo to the nginx config
    $ sudo ln -s /home/ubuntu/cov19.virusmodels.org/nginx/cov19.virusmodels.org /etc/nginx/sites-available
    $ sudo ln -s /home/ubuntu/cov19.virusmodels.org/nginx/cov19.virusmodels.org /etc/nginx/sites-enabled

    $ sudo rm /etc/nginx/default

    # restart so that the new config settings take effect.
    $ sudo nginx -t
    $ sudo systemctl restart nginx


User Guide
----------
No user documentation exists .... yet.

Custom Pages
^^^^^^^^^^^^

-  https://cov19.virusmodels.org/
-  https://cov19.virusmodels.org/admin/
-  https://cov19.virusmodels.org/login/
-  https://cov19.virusmodels.org/logout/
-  https://cov19.virusmodels.org/logged-out/
-  https://cov19.virusmodels.org/oauth-error/

User api:
^^^^^^^^^

-  https://cov19.virusmodels.org/o/api/users/
-  https://cov19.virusmodels.org/o/api/users/
-  https://cov19.virusmodels.org/o/api/groups/

**Additional Technical Documentation**

-  `medium.com - Deploying
   Django <https://medium.com/@_christopher/deploying-my-django-app-to-a-real-server-part-i-de78962e95ac>`__
-  `Digital Ocean - Deploying
   Django <https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04>`__
-  `oAuth Client - Python Social Auth
   Django <https://python-social-auth.readthedocs.io/en/latest/>`__
-  `oAuth Provider - Django oAuth Provider
   Toolkit <https://django-oauth-toolkit.readthedocs.io/en/latest/>`__
-  `Whitenoise with
   Django <http://whitenoise.evans.io/en/stable/django.html>`__
-  `Setting up a Django OAuth2 server &
   client <https://raphaelyancey.fr/en/2018/05/28/setting-up-django-oauth2-server-client.html>`__
-  `Custom Django User
   Model <https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser>`__
-  `Example oauth provider
   server <https://github.com/raphaelyancey/django-oauth2-example/blob/master/server/server/settings.py>`__
-  `Django oauth Toolkit -
   Github <https://github.com/jazzband/django-oauth-toolkit>`__
-  `Django oauth Toolkit -
   Documentation <https://django-oauth-toolkit.readthedocs.io/en/latest/settings.html>`__
-  `Guide to an OAuth2 API with Django -
   Medium.com <https://medium.com/@halfspring/guide-to-an-oauth2-api-with-django-6ba66a31d6d>`__

Scope
^^^^^

-  create CI procedures for local dev environement with code archived in
   private Github repos
-  create Ubuntu 18.04 LTS stack with letsencrypt SSL certificates
-  create custom User object with custom openstax tracking fields
-  create REST api for custom user object
-  add Bootstrap 4.x
