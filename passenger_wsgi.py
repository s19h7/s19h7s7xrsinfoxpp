# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/s/ccxvk419/ccxvk419.beget.tech/s1gh7t')
sys.path.insert(1, '/home/s/ccxvk419/ccxvk419.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 's1gh7t.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()