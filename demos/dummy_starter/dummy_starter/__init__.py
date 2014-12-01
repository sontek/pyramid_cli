from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
#    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello_world', '/')
    config.add_view(
        'dummy_starter.standard_views.hello_world',
        route_name='hello_world'
    )

    config.scan()
    return config.make_wsgi_app()
