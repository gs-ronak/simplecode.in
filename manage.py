import os
import sys
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
