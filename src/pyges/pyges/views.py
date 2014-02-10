# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound

def editcss_view(request):
	e = Estils.all()
	return { "listskins":e }
	
def updatecss_view(request):
	e = Estils.all()
	
	id = int(request.POST['skinselect'])
	
	for element in e:
		if element.id == id:
			contingut = element.contingut
			
	return{"contingut":contingut}
	
def confirmupdate_view(request):
	return {"edit":"edit skin"}

def createskin_view(request):
	return {"create":"create skin"}
	
def confirmcreate_view(request):
	id = int(request.POST['id'])
	nom = request.POST['nom']
	contingut = request.POST['contingut']
	
	estil = Estils(id=id,nom=nom,contingut=contingut)
	estil.put()
	
	return {"create":"create skin"}

def root_view(request):
	# show all pages
    p = Page.all()
    return { "pages":p }

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
    b = Page.all()
    return { "page": p , "pages":b}

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
