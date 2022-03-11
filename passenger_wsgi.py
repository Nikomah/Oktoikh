# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/o/octoechos/octoechos.beget.tech/my_own_site')
sys.path.insert(1, '/home/o/octoechos/.local/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = '<название_проекта>.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
