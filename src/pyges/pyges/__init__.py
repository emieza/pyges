from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))


def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator( root_factory=Root, settings=settings )
    config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)

    config.add_view(views.root_view,
                    context=Root,
                    renderer='root.mako')

    config.add_route( "view_page", "/view_page/{id}" )
    config.add_view( views.view_page_view, route_name="view_page", renderer="view_page.mako" )
    

    # ADMIN
    config.add_route( "create_page", "/create_page" )
    config.add_view( views.create_page_view, route_name="create_page", renderer="create_page.mako" )
    config.add_route( "admin_config", "/admin/config" )
    config.add_view( views.admin_config_view, route_name="admin_config", renderer="admin_config.mako" )

    # TRANSLATE
    config.add_route( "view_trans", "/view_trans" )
    config.add_view( views.view_trans_view, route_name="view_trans", renderer="view_trans.mako" )
    config.add_route( "edit_trans", "/edit_trans/{id}" )
    config.add_view( views.edit_trans_view, route_name="edit_trans", renderer="edit_trans.mako" )
    config.add_route( "create_trans", "/create_trans/{id}" )
    config.add_view( views.create_trans_view, route_name="create_trans", renderer="create_trans.mako" )
    config.add_route( "delete_trans", "/delete_trans/{fn}/{id}" )
    config.add_view( views.create_trans_view, route_name="delete_trans", renderer="delete_trans.mako" )

    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    
    return config.make_wsgi_app()

application = make_app()
