# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
from .base import *
import os
STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, "static")
