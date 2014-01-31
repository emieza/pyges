# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound

def root_view(request):
	# show all pages
    p = Page.all()
    f = Imatge.all()
    return { "pages":p, "imatges":f }


def create_page_view(request):
    if request.method=="GET":
    	# first visit: show form
        return {}
    # POST form: save page
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(title=title,text=text)
    page.put()
    return HTTPFound( "/" )#request.application_url )

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

def upload_view(request):
    if request.method=="GET":
        # first visit: show form
        return {}
    # POST form: save page
    titol = request.POST.get("titol")
    imatge = request.POST.get("imatge")
    imatge = db.Blob(str(imatge))

    categoria = request.POST.get("categoria")
    img = Imatge(titol=titol,imatge=imatge,categoria=categoria)
    img.put()
    return HTTPFound( "/" )#request.application_url )







