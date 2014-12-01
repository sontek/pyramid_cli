from pyramid.config import Configurator
from pyramid.security import Authenticated
from pyramid.security import Allow


class RootContext(object):
    def __init__(self, request):
        self.request = request

    @property
    def __acl__(self):
        return [(Allow, Authenticated, 'authenticated')]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view(name='static2', path='/var/www/static')
    config.add_static_view(
        name='pdt_images',
        path='pyramid_debugtoolbar:static/img/'
    )
    config.add_route('a', '')
    config.add_route('no_view_attached', '/')
    config.add_route('route_and_view_attached', '/')
    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='route_and_view_attached'
    )

    config.add_route('only_post_on_route', '/route', request_method='POST')
    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='only_post_on_route'
    )

    config.add_route('only_post_on_view', '/view')
    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='only_post_on_view',
        request_method='POST'
    )

    config.add_route(
        'method_intersection',
        '/intersection', request_method=('POST', 'PUT')
    )

    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='method_intersection',
        request_method='POST'
    )

    config.add_route(
        'method_conflicts',
        '/conflicts', request_method=('POST', 'PUT')
    )

    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='method_conflicts',
        request_method='PATCH'
    )

    config.add_route(
        'multiview',
        '/multiview',
    )

    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='multiview',
        request_method='PATCH'
    )

    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='multiview',
        request_method='GET'
    )

    config.add_view(
        'dummy_starter.standard_views.hello_world',
        route_name='multiview',
        request_method='POST'
    )

    config.add_route(
        'class_based_view',
        '/classes',
    )

    config.add_view(
        'dummy_starter.standard_views.ClassBasedView',
        attr='awesome',
        route_name='class_based_view',
        request_method='POST'
    )

    config.add_route(
        'factory',
        '/factory',
        factory=RootContext,
    )

    config.add_view(
        'dummy_starter.standard_views.route_and_view_attached',
        route_name='factory',
    )

    config.scan()
    return config.make_wsgi_app()
