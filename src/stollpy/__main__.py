import asyncio
import logging
import sys

import click

from ._version import __version__
from .api import api
from .scheduler import scheduler
from .web import web

__all__ = ["api", "scheduler", "web"]


@click.group("app")
@click.pass_context
def app(ctx):
    pass


app.add_command(api)
app.add_command(scheduler)
app.add_command(web)


def main(args=None):
    # parser = ArgumentParser()
    # parser.add_argument("--version", action="version", version=__version__)
    # args = parser.parse_args(args)
    if len(args) == 2 and args[1] == '--version':
        return print(__version__)
    else:
        return asyncio.run(app(prog_name="scheduler"))

if __name__ == "__main__":
    logger = logging.getLogger("stollander")
    logger.addHandler(logging.StreamHandler())

    sys.exit(main(sys.argv))
