from pyramid.tweens import MAIN
from pyramid.tweens import INGRESS
from pyramid.config import Configurator
from pyramid.interfaces import ITweens
import click


def get_tweens(registry):
    config = Configurator(registry=registry)
    return config.registry.queryUtility(ITweens)


def show_chain(chain):
    fmt = '%-10s  %-65s'
    click.echo(fmt % ('Position', 'Name'))
    click.echo(fmt % ('-'*len('Position'), '-'*len('Name')))
    click.echo(fmt % ('-', INGRESS))
    for pos, (name, _) in enumerate(chain):
        click.echo(fmt % (pos, name))

    click.echo(fmt % ('-', MAIN))


@click.command()
@click.pass_context
def tweens_cli(ctx):
    registry = ctx.obj['env']['registry']
    tweens = get_tweens(registry)

    if tweens is not None:
        explicit = tweens.explicit

        if explicit:
            click.echo(
                '"pyramid.tweens" config value set '
                '(explicitly ordered tweens used)'
            )
            click.echo('')
            click.echo('Explicit Tween Chain (used)')
            click.echo('')

            show_chain(tweens.explicit)

            click.echo('')
            click.echo('Implicit Tween Chain (not used)')
            click.echo('')

            show_chain(tweens.implicit())
        else:
            click.echo(
                '"pyramid.tweens" config value NOT set '
                '(implicitly ordered tweens used)'
            )
            click.echo('')
            click.echo('Implicit Tween Chain')
            click.echo('')

            show_chain(tweens.implicit())
