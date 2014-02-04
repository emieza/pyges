# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound
langs={"en":"English","es":"Español","ca":"Català"}
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

# translation functions

def view_trans_view(request):
    global langs
    pages = Page.all()
    ids = [] # list of secondary id (language group)
    tbl = [] # table of titles and id for each language
    for page in pages:
        if not page.idsec in ids:
            ids.append(page.idsec)
            if page.lang == "en":
                tbl.append({"idsec":page.idsec,"title_en":page.title,"title_es":"","title_ca":"","id_en":page.key().id(),"id_es":"","id_ca":""})
            if page.lang == "es":
                tbl.append({"idsec":page.idsec,"title_en":"","title_es":page.title,"title_ca":"","id_en":"","id_es":page.key().id(),"id_ca":""})
            if page.lang == "ca":
                tbl.append({"idsec":page.idsec,"title_en":"","title_es":"","title_ca":page.title,"id_en":"","id_es":"","id_ca":page.key().id()})
        else:
            for i in range(len(tbl)):
                if page.idsec == tbl[i]["idsec"]:
                    if page.lang == "en":
                    	tbl[i]["title_en"] = page.title
                        tbl[i]["id_en"] = page.key().id()
                    if page.lang == "es":
                    	tbl[i]["title_es"] = page.title
                        tbl[i]["id_es"] = page.key().id()
                    if page.lang == "ca":
                    	tbl[i]["title_ca"] = page.title
                        tbl[i]["id_ca"] = page.key().id()
    return {"table":tbl,"langs":langs}

def create_trans_view(request):
    global langs
    if request.method=="GET":
        # first visit: show form
        id = int(request.matchdict['id'])
        p = Page.get_by_id(id)
        pages = Page.all()
        lex = [] # existent languages
        lex.append("none")
        for page in pages:
            if p.idsec == page.idsec:
                lex.append(page.lang)
        lop = langs.copy() # option languages
        lop["none"] = "none"
        for l in lex:
            del lop[l]
        return {"page":p, "langs":langs, "lop":lop}
    # POST form: save translation page
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
        fn = request.matchdict['fn'] # function one (delete language page), all (delete all pages)
        id = int(request.matchdict['id']) # function one (id), function all (idsec)
        if fn == "one":
        	pass
        if fn == "all":
            pass
        p = Page.get_by_id(id)
        return {"pages":p,"langs":langs}
    # POST form: delete translation page or page
    confirm = request.POST.get("confirm")
    if confirm == "ok":
        pass
    return HTTPFound( "/" )#request.application_url )	
