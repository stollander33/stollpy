import os
import sys
from importlib.metadata import version

__version__ = version("stollpy")
del version

folder = os.path.join(os.path.dirname(os.path.dirname(__file__)))
if not folder in sys.path:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))

__all__ = ["__version__", "api", "scheduler", "web"]
