import datetime

from pyramid.view import view_config


@view_config(renderer='templates/google.jinja2', request_method='GET', route_name='cluster_map')
def cluster_map(request):
    return {}