import logging
import os
import sys

from stollpy.api import app as app_fastapi
from stollpy.scheduler import app as app_rocketry

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
