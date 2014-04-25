from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder

__here__ = os.path.dirname(os.path.abspath(__file__))

def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')  
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator( root_factory=Root, settings=settings )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    
    config.add_view(views.root_view, context=Root, renderer='root.mako')

    config.add_route( "view_page", "/view_page/{id}" )
    config.add_view( views.view_page_view, route_name="view_page", renderer="view_page.mako" )

    # GALLERY
    # Defined route and view for the upload template
    config.add_route( "upload", "/upload" )
    config.add_view( views.upload_view, route_name="upload", renderer="upload.mako")
    # Defined routes and name for the view (without template, directly returns image)
    config.add_route( "view_picture", "/view_picture/{id}" )
    config.add_view( views.view_picture_view, route_name="view_picture")
    # Defined routes and name for the gallery (request and render all uploaded images)
    config.add_route( "view_all_images", "/view_all_images" )
    config.add_view( views.view_all_images_view, route_name="view_all_images", renderer="view_all_images.mako")

    # ADMIN
    config.add_route( "create_page", "/create_page" )
    config.add_view( views.create_page_view, route_name="create_page", renderer="create_page.mako" )
    config.add_route( "admin_config", "/admin/config" )
    config.add_view( views.admin_config_view, route_name="admin_config", renderer="admin_config.mako" )
    
    # MAIL
    config.add_route("send_mail","/send_mail")
    config.add_view(views.send_mail,route_name="send_mail", renderer="send_mail.mako")

    # TRANSLATE
    config.add_route( "trans_menu", "/trans_menu" )
    config.add_view( views.trans_menu_view, route_name="trans_menu", renderer="trans_menu.mako" )
    config.add_route( "trans_edit", "/trans_edit/{id}" )
    config.add_view( views.trans_edit_view, route_name="trans_edit", renderer="trans_edit.mako" )
    config.add_route( "trans_create", "/trans_create/{ln}/{id}" )
    config.add_view( views.trans_create_view, route_name="trans_create", renderer="trans_create.mako" )
    config.add_route( "trans_view", "/trans_view/{ln}/{id}" )
    config.add_view( views.trans_view_view, route_name="trans_view", renderer="trans_view.mako" )
    config.add_route( "trans_delete", "/trans_delete/{fn}/{id}" )
    config.add_view( views.trans_delete_view, route_name="trans_delete", renderer="trans_delete.mako" )
    
    # SKIN & CSS
    config.add_route('login', '/login')
    config.add_view( views.login, route_name="login", renderer="templates/login.pt" )
    config.add_route('logout', '/logout')
    config.add_view( views.logout, route_name="logout", renderer="templates/logout.pt" )

    config.add_route( "createskin", "/createskin" )
    config.add_view( views.createskin_view, route_name="createskin", renderer="createskin.mako" )
    config.add_route( "confirmcreate", "/confirmcreate" )
    config.add_view( views.confirmcreate_view, route_name="confirmcreate", renderer="confirmcreate.mako" )
    config.add_route( "editcss", "/editcss" )
    config.add_view( views.editcss_view, route_name="editcss", renderer="editcss.mako" )
    config.add_route( "updatecss", "/updatecss" )
    config.add_view( views.updatecss_view, route_name="updatecss", renderer="updatecss.mako" )  
    config.add_route( "confirmupdate", "/confirmupdate" )
    config.add_view( views.confirmupdate_view, route_name="confirmupdate", renderer="confirmupdate.mako" )

    config.add_static_view(name='static', path=os.path.join(__here__, 'static'))
    config.scan()    
    return config.make_wsgi_app()

    
application = make_app()
