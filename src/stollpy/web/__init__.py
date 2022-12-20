import click

from stollpy.api.v1.tasks import app


@click.group("web")
@click.pass_context
def web(ctx):
    pass


@click.command("compile")
@click.option("-d", "--download", is_flag=True, help="Pass to download the result to a json file")
@click.option("-k", "--key", help="Pass a key to specify that key from the results")
@click.pass_context
def compile(ctx, download: bool, key: str):
    click.echo('compile %s the %s database' % (download, key))


@click.command("start")
@click.option('--debug', default=True,   help='Arancar con depurador')
def start(debug):
    click.echo(f"Hello {debug}!")


@click.command("stop")
@click.option('--force', default=False, help='Force to stop wen')
def stop(force):    
    click.echo('Dropped the database %s ' % force)


web.add_command(compile)
web.add_command(start)
web.add_command(stop)
