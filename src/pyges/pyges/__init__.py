from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))

def make_app():
	""" This function returns a Pyramid WSGI application."""
	settings = {}
	settings['mako.directories'] = os.path.join(__here__, 'templates')
	config = Configurator( root_factory=Root, settings=settings )
	config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
	
	config.add_view(views.root_view, context=Root, renderer='root.mako')
	
	config.add_route( "view_page", "/view_page/{id}" )
	config.add_view( views.view_page_view, route_name="view_page", renderer="view_page.mako" )
	
	# ADMIN
	config.add_route( "create_page", "/create_page" )
	config.add_view( views.create_page_view, route_name="create_page", renderer="create_page.mako" )
	config.add_route( "admin_config", "/admin/config" )
	config.add_view( views.admin_config_view, route_name="admin_config", renderer="admin_config.mako" )
	
	#CREATE CSS
	config.add_route( "createskin", "/createskin" )
	config.add_view( views.createskin_view, route_name="createskin", renderer="createskin.mako" )
	
	#CONFIRM CREATE CSS
	config.add_route( "confirmcreate", "/confirmcreate" )
	config.add_view( views.confirmcreate_view, route_name="confirmcreate", renderer="confirmcreate.mako" )
	
	#EDIT CSS
	config.add_route( "editcss", "/editcss" )
	config.add_view( views.editcss_view, route_name="editcss", renderer="editcss.mako" )
	
	#UPDATE CSS
	config.add_route( "updatecss", "/updatecss" )
	config.add_view( views.updatecss_view, route_name="updatecss", renderer="updatecss.mako" )
	
	#CONFIRM UPDATE CSS
	config.add_route( "confirmupdate", "/confirmupdate" )
	config.add_view( views.confirmupdate_view, route_name="confirmupdate", renderer="confirmupdate.mako" )
	
	config.add_static_view(name='static',path=os.path.join(__here__, 'static'))
	
	return config.make_wsgi_app()
	
application = make_app()
