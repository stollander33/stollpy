"""Console script for stoll_py."""
import asyncio
import logging
import os
import sys

import click
import uvicorn

from stollpy.api import app as tasks
from stollpy.scheduler import app as app_rocketry

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
# sys.path.append('/path/to/dir')

logger = logging.getLogger("stollpy")
logger.addHandler(logging.StreamHandler())


@click.command()
def main(args=None):
    """Console script for stoll_py."""
    click.echo("Replace this message by putting your code into " "stoll_py.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return asyncio.run(_main())


@click.command()
def api(args=None):
    """Console script for stoll_py."""
    click.echo("Replace this message by putting your code into " "stoll_py.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return asyncio.run(_api())


class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def _main():
    logger.debug(sys.path)
    print(sys.path)
    "Run Rocketry and FastAPI"
    server = Server(config=uvicorn.Config(tasks, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())

    sched = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([sched, api])


async def _api():
    "Run Rocketry and FastAPI"
    server = Server(config=uvicorn.Config(tasks, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())

    await asyncio.wait([api])


if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("rocketry.task")
    logger.addHandler(logging.StreamHandler())

    logger.debug(sys.path)
    # Run both applications
    sys.exit(main())
