import pytest

from click.testing import CliRunner
from tests.utils import get_demo_path


@pytest.mark.integration
def test_basic_tween():
    from pyramid_cli import cli

    runner = CliRunner()
    ini_path = get_demo_path('dummy_starter/development.ini')
    result = runner.invoke(
        cli, [ini_path, 'tweens']
    )
    expected_output = """\
"pyramid.tweens" config value NOT set (implicitly ordered tweens used)

Implicit Tween Chain

Position    Name
--------    ----
-           INGRESS
0           pyramid_debugtoolbar.toolbar_tween_factory
1           pyramid.tweens.excview_tween_factory
-           MAIN"""

    assert result.exit_code == 0

    final_output = result.output.split('\n')

    for index, line in enumerate(expected_output.split('\n')):
        assert line.strip() == final_output[index].strip()


@pytest.mark.integration
def test_basic_explicit_tween():
    from pyramid_cli import cli

    runner = CliRunner()
    ini_path = get_demo_path('dummy_starter/explicit_tweens.ini')
    result = runner.invoke(
        cli, [ini_path, 'tweens']
    )

    expected_output = """\
"pyramid.tweens" config value set (explicitly ordered tweens used)

Explicit Tween Chain (used)

Position    Name
--------    ----
-           INGRESS
0           pyramid_debugtoolbar.toolbar_tween_factory
1           pyramid.tweens.excview_tween_factory
-           MAIN"""

    assert result.exit_code == 0

    final_output = result.output.split('\n')

    for index, line in enumerate(expected_output.split('\n')):
        assert line.strip() == final_output[index].strip()
