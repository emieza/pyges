# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound

# http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/humans/forms_schemas/
from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf

from deform import ValidationFailure
from deform import Form
from deform import widget

def root_view(request):
	# show all pages
    p = Page.all()
    return { "pages":p }

class PageSchema(MappingSchema):
    title = SchemaNode(String())
    text = SchemaNode(Integer())

def create_page_view(request):
    """if request.method=="GET":
    	# first visit: show form
        return {}
    # POST form: save page
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(title=title,text=text)
    page.put()
    return HTTPFound( "/" )#request.application_url )"""
    schema = PageSchema()
    form = Form(schema,buttons=("submit",))
    return {"form":form.render()}

def view_page_view(request):
	# show a particular page
    id = int(request.matchdict['id'])
    p = Page.get_by_id(id)
    return { "page": p }

def admin_config_view(request):
    # config should be a singleton
    config = GlobalConfig.all().get()
    if not config:
        print "creanting initial site config..."
        config = GlobalConfig(
            site_name = "Pyges Site",
            admin_users = []
        )
    # TODO: check singleton (only one instance)
    
    # data have been sent: update site config
    if request.method=="POST":
        site_name = request.POST.get("sitename")
        admin_users = request.POST.get("adminusers")
        config.site_name = site_name
        config.admin_users = admin_users.split()
        config.put()
    return {"config":config}
