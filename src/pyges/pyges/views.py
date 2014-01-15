# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound

# http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/humans/forms_schemas/
# widget summary
# http://deformdemo.repoze.org/
import colander, deform
from colander import Schema
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

class PageSchema(Schema):
    title   = SchemaNode(String())
    text    = SchemaNode( String(),
                    #validator = Length(max=100),
                    #widget = widget.TextAreaWidget(rows=10,cols=60),
                    widget = widget.RichTextWidget(),
                    description = "Write your page text here"
                )

def create_page_view(request):
    schema = PageSchema()
    form = Form( schema, buttons=("submit",) )
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except ValidationFailure, e:
            return {'form':e.render(), 'values': False}
        # Process the valid form data, do some work
        values = {
            "title": appstruct['title'],
            "text": appstruct['text'],
            }
        return {"form": form.render(), "values": values}
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
