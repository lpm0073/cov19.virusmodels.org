#!/usr/bin/env python
import os
import sys

# lawrence: use .env to control environment
import dotenv

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    # mcdaniel:
    # this allows us to seamlessly toggle between local (ie "dev") and production settings.
    # .env contains the DJANGO_SETTINGS_MODULE value:
    #           "config.settings.local" for dev,
    #           "config.settings.production" for AWS Ubuntu
    # reference: https://github.com/jpadilla/django-dotenv
    # this needs to be placed immediately above os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    dotenv.read_dotenv(override=True)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # cov19 directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "cov19"))

    execute_from_command_line(sys.argv)
