"""Console script for stoll_py."""
import asyncio

import click
import uvicorn

from stollpy.api.v1.tasks import app as app_api
from stollpy.scheduler.v1.rocketry import app as app_rocketry


class Server(uvicorn.Server):
    """Customized uvicorn.Server
    
    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""
    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def _api():
    "Run Rocketry and FastAPI"
    server = Server(config=uvicorn.Config(app_api, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())

    await asyncio.wait([api])


@click.group("api")
@click.pass_context
def api(ctx):
    pass


@click.command("start")
@click.option("-d", "--debug", default=True, is_flag=True, help="Pass to download the result to a json file")
@click.pass_context
def start(ctx, debug: bool):
    """
    Start API server
    """
    click.echo('start_api %s debug ' % (debug))
    # server = Server(config=uvicorn.Config(app_api, workers=1, loop="asyncio"))
    # api = asyncio.create_task(server.serve())    
    return asyncio.run(_api())


@click.command("stop")
@click.option("-d", "--force", default=False, is_flag=True, help="Stop API server")
@click.pass_context
def stop(ctx, force):
    """
    Stop API server. (force: fuerza la parada de procesos en curso)
    """
    return click.echo(f"Hello {force}!")


@click.command("create_user")
@click.option('--admin', default=False, help='Is superuser?')
@click.argument("name")
@click.argument('password')
@click.pass_context
def create_user(ctx, admin: bool , name: str, password: str):
    """
    Crear un usuario
    """
    click.echo('%s es super? %s' % (name, admin))


api.add_command(create_user)
api.add_command(start)
api.add_command(stop)
