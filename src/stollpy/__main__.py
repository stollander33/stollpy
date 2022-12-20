import logging
import os
import sys

from .cli import main

__all__ = ["main"]

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))

if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("stollander")
    logger.addHandler(logging.StreamHandler())
    
    sys.exit(main())

