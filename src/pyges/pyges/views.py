# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound
langs={"en":"English","ca":"Català","es":"Español"}
firstp=False

def root_view(request):
    global langs
	# show all pages
    p = Page.all()
    return { "pages":p,"langs": langs}

def create_page_view(request):
    global langs
    if request.method=="GET":
    	# first visit: show form
        return {"langs": langs}
    
    # POST form: save page
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(lang=lang,title=title,text=text)
    page.put() #desa a la BBDD
    page.idsec = int(page.key().id())
    page.put()
    return HTTPFound( "/" ) #request.application_url )

def view_page_view(request):
    global langs
	# show a particular page
    id = int(request.matchdict['id'])
    #crear id2(copia id) + id idioma
    p = Page.get_by_id(id)
    return { "page": p, "langs":langs}

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

# translate functions

def view_trans_view(request):
    global langs
    pages = Page.all()
    p = list_trans(pages)
    return {"pages":p, "langs":langs}

def create_trans_view(request):
    global langs
    if request.method=="GET":
        # first visit: show form
        id = int(request.matchdict['id'])
        p = Page.get_by_id(id)
        return {"page":p, "langs":langs}
    # POST form: save page
    idsec = int(request.POST.get("idsec"))
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(idsec=idsec,lang=lang,title=title,text=text)
    page.put() #desa a la BBDD
    return HTTPFound( "/" )#request.application_url )

def delete_trans_view(request):
    if request.method=="GET":
        # first visit: show form
        fn = request.matchdict['fn']
        id = int(request.matchdict['id'])
        pages = Page.all()
        if fn == "one": # delete one translation (id)
        	pass
        if fn == "all": # delete all translation (idsec)
            pass
        p = Page.get_by_id(id)
        return {"pages":p, "langs":langs}
    # POST form: delete page
    confirm = request.POST.get("confirm")
    if confirm == 0:
        # all pages
        pass
    if confirm == 1:
        # only translate
        pass
    return HTTPFound( "/" )#request.application_url )


def list_trans(pages):
    ids = [] # list secondary id (language group)
    p = [] # list of pages ordered by secondary id
    for pag in pages:
        if not pag.idsec in ids:
            ids.append(pag.idsec)
            pag.jump = True
            p.append(pag)
        else:
            for i in range(len(p)):
                if pag.idsec == p[i].idsec:
                    pag.jump = True
                    p[i].jump = False
                    p.insert(i+1,pag)
                    break
    return p	
