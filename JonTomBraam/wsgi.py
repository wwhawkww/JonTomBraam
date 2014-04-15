"""
WSGI config for JonTomBraam project.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JonTomBraam.settings")

# -Original- the original implimentation
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
