import click
from pyramid.paster import bootstrap
from .tweens import tweens_cli


def get_pyramid_env(config_uri):
    env = bootstrap(config_uri)

    return env


@click.group()
@click.argument('config_uri')
@click.pass_context
def cli(ctx, config_uri):
    """
    CLI utility for managing pyramid
    """
    ctx.obj = {
        'env': get_pyramid_env(config_uri)
    }
    return ctx

cli.add_command(tweens_cli, name='tweens')
