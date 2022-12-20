import os
import sys
from importlib.metadata import version

__version__ = version("stollpy")
del version

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
print(os.path.join(os.path.dirname(os.path.dirname(__file__))))
__all__ = ["__version__","api","scheduler","web"]

print(sys.path)
