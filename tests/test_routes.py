import pytest

from click.testing import CliRunner
from tests.utils import get_demo_path


@pytest.mark.integration
def test_basic_routes():
    from pyramid_cli import cli
    runner = CliRunner()
    ini_path = get_demo_path('dummy_starter/development.ini')

    result = runner.invoke(
        cli, [ini_path, 'routes']
    )
    assert result.exit_code == 0
