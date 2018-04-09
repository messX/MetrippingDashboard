# package
from pyramid.config import Configurator

# def initialize_redis_db(config):
#     conn = _Redis(host=CONF.REDIS_MAIN)
#     config.registry.settings['!redis_conn'] = conn
#     config.add_request_method(
#         add_redis_db, name='redis_conn', reify=True)

# def add_redis_db(request):
#     settings = request.registry.settings
#     return settings['!redis_conn']

def main(_, **settings):
    config = Configurator(settings=settings)
    # initialize_redis_db(config)
    config.include('pyramid_jinja2')
    config.add_static_view(name='static', path='./static')
    config.add_route('cluster_map', '/cluster/map')
    config.add_route('experience', '/experience')
    config.scan('.views')

    return config.make_wsgi_app()
