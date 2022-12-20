"""
Console script for stollpy
"""
import asyncio
import logging

import click
import uvicorn

from stollpy import _version
from stollpy.api import app as tasks
from stollpy.scheduler import app as app_rocketry

logger = logging.getLogger("stollpy")
logger.addHandler(logging.StreamHandler())


@click.command()
def version(count=1, name=None):
    """
    Console script for stoll_py.
    """
    click.echo(_version)
    return _version


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default="Richi", prompt='Your name', help='The person to greet.')
def main(count=1, name=None):
    """
    Console script for stoll_py.
    """
    click.echo("%s Replace this message by putting your code into stoll_py.cli.main" % name)
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return asyncio.run(_main())


@click.command()
@click.option("--show_docs", default=True, help="Mostrar/Ocultar la documentación.")
@click.option("--production", default=False, help="Ejecutar en modo production")
def api(show_docs, production):
    """
    Console script for stoll_py.
    """
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
    logger = logging.getLogger("stollpy")
    logger.addHandler(logging.StreamHandler())

    # Run both applications
    asyncio.run(_main())
