import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_luciano_martins.settings")

application = get_wsgi_application()
app = get_wsgi_application()