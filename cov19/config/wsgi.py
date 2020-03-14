"""
WSGI config for cov19.virusmodels.org project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

# lawrence: use .env files to control environment
import dotenv

from django.core.wsgi import get_wsgi_application

DEBUG = True

# This allows easy placement of apps within the interior
# cov19 directory.
root_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
config_path = os.path.join(root_path, "config")
env_path = os.path.join(root_path, '.env')
app_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
sys.path.append(os.path.join(app_path, "cov19"))
sys.path.append(root_path)
sys.path.append(config_path)

if DEBUG:
    print('wsgi.py root_path: {path}'.format(path=root_path))
    print('wsgi.py app_path: {path}'.format(path=app_path))
    print('wsgi.py config_path: {path}'.format(path=config_path))
    print('wsgi.py env_path: {path}'.format(path=env_path))

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# mcdaniel:
# this allows us to seamlessly toggle between local (ie "dev") and production settings.
# .env contains the DJANGO_SETTINGS_MODULE value:
#           "config.settings.local" for dev,
#           "config.settings.production" for AWS Ubuntu
# reference: https://github.com/jpadilla/django-dotenv
# this needs to be placed immediately above os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
dotenv.read_dotenv(env_path, override=True)

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

