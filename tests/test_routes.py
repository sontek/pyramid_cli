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

    expected_output = """\
Name                       Pattern                     View                                                    Method
-----------------------    ------------------------    -----------------------------------------------------   ----------------
debugtoolbar               /_debug_toolbar/*subpath    <wsgiapp>                                               *
__static/                  /static/*subpath            dummy_starter:static/                                   *
__static2/                 /static2/*subpath           /var/www/static/                                        *
__pdt_images/              /pdt_images/*subpath        pyramid_debugtoolbar:static/img/                        *
a                          /                           <unknown>                                               *
no_view_attached           /                           <unknown>                                               *
route_and_view_attached    /                           dummy_starter.standard_views.route_and_view_attached    *
only_post_on_route         /route                      dummy_starter.standard_views.route_and_view_attached    POST
only_post_on_view          /view                       dummy_starter.standard_views.route_and_view_attached    POST
method_intersection        /intersection               dummy_starter.standard_views.route_and_view_attached    POST
method_conflicts           /conflicts                  dummy_starter.standard_views.route_and_view_attached    <route mismatch>
multiview                  /multiview                  dummy_starter.standard_views.route_and_view_attached    PATCH,GET
multiview                  /multiview                  dummy_starter.standard_views.hello_world                POST
class_based_view           /classes                    dummy_starter.standard_views.ClassBasedView.awesome     POST
"""  # noqa
    assert result.exit_code == 0
    final_output = result.output.split('\n')

    for line_index, line in enumerate(expected_output.split('\n')):
        columns = final_output[line_index].strip().split()
        for col_index, column in enumerate(line.strip().split()):
            # Skip the separator
            if '-------' in column:
                continue

            assert column.strip() == columns[col_index].strip()
