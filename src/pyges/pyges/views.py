# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound
langs={"es":"Spanish","ca":"Català","en":"English"}
firstp=False

def root_view(request):
	# show all pages
    p = Page.all()
    return { "pages":p }

def create_page_view(request):
    global langs
    if request.method=="GET":
    	# first visit: show form
        return {"langs": langs}
    
    # POST form: save page
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(title=title,text=text)
    page.put() #desa a la BBDD
    page.idsec = page.key().id()
    page.put()
    return { HTTPFound( "/" )}#request.application_url )

def view_page_view(request):
	# show a particular page
    id = int(request.matchdict['id'])
    #crear id2(copia id) + id idioma
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
    
def view_trans_view(request):
	# show a particular page
    id = int(request.matchdict['id'])
    #crear id2(copia id) + id idioma
    p = Page.get_by_id(id)
    return { "page": p }

def create_trans_view(request):
    global langs
    if request.method=="GET":
    	# first visit: show form
        return {"langs": langs}
    
    # POST form: save page
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(title=title,text=text)
    page.put() #desa a la BBDD
    page.idsec = page.key().id()
    page.put()
    return { HTTPFound( "/" )}#request.application_url )

