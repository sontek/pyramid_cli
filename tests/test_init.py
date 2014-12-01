import pytest

from click.testing import CliRunner
from tests.utils import get_demo_path


@pytest.mark.integration
def test_core_empty():
    from pyramid_cli import cli

    runner = CliRunner()
    ini_path = get_demo_path('dummy_starter/development.ini')

    result = runner.invoke(
        cli, [ini_path]
    )

    assert 'Usage: cli [OPTIONS] CONFIG_URI' in result.output
    assert result.exit_code == 2


@pytest.mark.integration
def test_core_help():
    from pyramid_cli import cli

    runner = CliRunner()
    ini_path = get_demo_path('dummy_starter/development.ini')

    result = runner.invoke(
        cli, [ini_path, '--help']
    )

    assert 'Usage: cli [OPTIONS] CONFIG_URI' in result.output
    assert cli.short_help in result.output
    assert result.exit_code == 0
