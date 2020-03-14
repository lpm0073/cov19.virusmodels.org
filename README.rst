cov19.virusmodels.org
=====================
.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

.. image:: https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg
     :target: https://lawrencemcdaniel.com
     :alt: Hack.d Lawrence McDaniel

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

Python Django Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a virtual environment, then activate it and install all pip
requirements. Also, run migrations, load initial data (if any), and
start the dev web server to ensure that the site comes up:

.. code:: bash

    $ git clone https://github.com/lpm0073/cov19.virusmodels.org.git
    $ cd cov19.virusmodels.org
    $ python3.7 -m venv venv
    $ source venv/bin/activate

2. Install Python requirements

.. code:: bash


    $ pip install --upgrade pip
    $ pip install -r cov19/requirements/local.txt



3. Create a new PostgreSQL database

.. code:: bash

    $ createdb cov19 -U postgres --password cov19

4. Set environment variable

.. code:: bash

    $ export DATABASE_URL=postgres://postgres:cov19@127.0.0.1:5432/cov19
    $ export CELERY_BROKER_URL=redis://localhost:6379/0

5. Bootstrap Django locally 

.. code:: bash

    $ cov19/manage.py migrate
    $ cov19/manage.py createsuperuser
    $ cov19/manage.py runserver


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

    # harden security on mysql
    mysql_secure_installation

    $ mysql -u root -p
    mysql> CREATE DATABASE cov19 CHARACTER SET 'utf8';
    mysql> CREATE USER cov19;
    mysql> GRANT ALL ON cov19.* TO 'cov19'@'localhost' IDENTIFIED BY 'cov19';
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

    ./manage.py makemigrations auth
    ./manage.py makemigrations admin
    ./manage.py makemigrations base
    ./manage.py makemigrations blog
    ./manage.py makemigrations breads
    ./manage.py makemigrations locations
    ./manage.py makemigrations search
    ./manage.py makemigrations users

Python Django Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    cd ~
    sudo rm -r ./cov19.virusmodels.org
    git clone git@github-cov19virusmodels:lpm0073/cov19.virusmodels.org.git

    python3 -m venv ~/cov19.virusmodels.org/venv
    source ~/cov19.virusmodels.org/venv/bin/activate
    pip install -r ~/cov19.virusmodels.org/cov19/requirements/production.txt

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

Point .env file to production

::

    vim /home/ubuntu/cov19.virusmodels.org/.env
    DJANGO_SETTINGS_MODULE=cov19.settings.production
    DJANGO_SECRET_KEY = 'A STRONG KEY THAT IS USED BY DJANGO.'

Point cov19/wsgi.py to production

::

    vim /home/ubuntu/cov19.virusmodels.org/cov19/wsgi.py
    DELETE THIS ---> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cov19.settings.production")

Add a cov19.virusmodels.org/cov19/settings/passwords.py file with values
for

::


    MYSQL_COV19_PWD = 'YOUR TOP-SECRET PASSWORD'

Initiate the Django build sequence to initialize the database, load
Wagtail sample data, compile static assets and finally, test the build
by starting the development web server. If there are no errors generated
from the web server launch then the built might have been successful.

::

    $ cd ~/cov19.virusmodels.org
    $ source ~/cov19.virusmodels.org/venv/bin/activate
    (env) $ python manage.py makemigrations
    (env) $ python manage.py migrate
    (env) $ python manage.py load_initial_data
    (env) $ python manage.py collectstatic
    (env) $ python manage.py runserver
    (env) $ deactivate

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

