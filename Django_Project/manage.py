#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Acts as a commmand-line tool that allows us to run special commands and do things like
make database migrations, run our Python server, create users for our Django admin pannel

this is a wrapper around django admin, but it also takes the settings of this project into account
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
