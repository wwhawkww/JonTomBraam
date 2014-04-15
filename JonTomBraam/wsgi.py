"""
WSGI config for JonTomBraam project.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JonTomBraam.settings")

# -Original- the original implimentation
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

#-Heroku- The required wsgi configuration due to dj_static
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())