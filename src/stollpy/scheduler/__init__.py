import asyncio

import click

from stollpy.scheduler.v1.rocketry import app
from stollpy.scheduler.v1.rocketry import do_fail as run_do_fail
from stollpy.scheduler.v1.rocketry import do_long as run_db_long
from stollpy.scheduler.v1.rocketry import do_permanently as run_do_permanently
from stollpy.scheduler.v1.rocketry import do_short as run_do_short


@click.group("scheduler")
@click.pass_context
def scheduler(ctx):
    pass


@click.command("do_fail")
@click.option('--background', default=True, help='Ejecuta una tarea (en background)')
def do_fail(background):
    """
    Ejecuta do_fail
    """
    return asyncio.run(run_do_fail())


@click.command("do_long")
@click.option('--force', default=False, help='Forece to terminate active tasks')
def do_long(force):
    """
    Ejecuta db_long
    """
    return asyncio.run(run_db_long())


@click.command("do_permanently")
@click.option('--force', default=False, help='Force to terminate active tasks')
def do_permanently(force):
    """
    Ejecuta do_permanently
    """
    return asyncio.run(run_do_permanently())


@click.command("do_short")
@click.option('--force', default=False, help='Forece to terminate active tasks')
def do_short(force):
    """
    Ejecuta do_short
    """
    return asyncio.run(run_do_short())


scheduler.add_command(do_permanently)
scheduler.add_command(do_short)
scheduler.add_command(do_fail)
scheduler.add_command(do_long)
