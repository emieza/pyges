# -*- coding: utf-8 -*-


from models import *
from pyramid.httpexceptions import HTTPFound
from google.appengine.api import mail
from google.appengine.api import users
from pyramid.response import Response

class Last():
	def __init__(self):
		self.lastskin = ""

last = Last()

def editcss_view(request):
	e = Estils.all()
	return { "listskins":e }
	
def updatecss_view(request):
	e = Estils.all()
	
	id = int(request.POST['skinselect'])
	
	for element in e:
		if element.id == id:
			contingut = element.contingut
			
	return{"id":id,"contingut":contingut}
	
def confirmupdate_view(request):
	e = Estils.all()
	contingut = request.POST['contingut']
	id = int(request.POST['id'])
	
	for element in e:
		if element.id == id:
			element.contingut = contingut
			element.put()
	
	
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
    # Contents all images
    pic = Picture.all()
    return { "pages":p, "pictures": pic, "langs": langs() }


def create_page_view(request):
    if request.method=="GET":
    	# first visit: show form
        return {"langs": langs()}
    # POST form: save page
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(lang=lang,title=title,text=text)
    page.put() #desa a la BBDD
    page.idsec = int(page.key().id())
    page.put()
    return HTTPFound( "/" ) #request.application_url )

    
def send_mail(request):
     if request.method=="GET":
    	# first visit: show form
        return {}
     # POST form: send mail
     try:
     	fname=request.POST["firstname"]
 	sname=request.POST["surname"]
	email=request.POST["mail"]
	msg=request.POST["text"]
	if fname=="" or sname=="" or email=="" or msg=="":
		return {'missatge':'Fill all the fields'}
     except:
	return {'missatge':'Fill all the fields'}
     message_body = "<h3>"+ fname + " " + sname + "</h3><h5>" + email + "</h5>" + msg
     mail.send_mail(
     sender='sundavar.l2@gmail.com',
     to='sundavar.l2@gmail.com',
     subject='Contact page '+fname+' '+sname,
     body=fname+" "+sname+" "+email+" "+msg,     
     html=message_body)
     return{'missatge':'Message sent'}


def view_page_view(request):
	if request.method=="POST":
		idd = int(request.POST['skinselect'])
		e = Estils.all()
		for element in e:
			if element.id == idd:
				last.lastskin = element.contingut
				
		# show a particular page
		id = int(request.matchdict['id'])
		p = Page.get_by_id(id)
		b = Page.all()
		return { "page": p , "pages":b, "contingut":last.lastskin, "listskins":e, "langs":langs() }
	else:
		# show a particular page
		e = Estils.all()
		id = int(request.matchdict['id'])
		p = Page.get_by_id(id)
		b = Page.all()
		return { "page": p , "pages":b, "listskins":e, "contingut":last.lastskin, "langs":langs() }


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


# Function for upload images
def upload_view(request):
    if request.method=="GET":
        # first visit: show form
        return {}
    # POST form: save image
    # Get image attributes
    title = request.POST.get("title")
    picture = request.POST.get("image").file.read()
    blob = db.Blob(picture)
    category = request.POST.get("category")
    img = Picture(title=title,image=blob,category=category)
    img.put()
    return HTTPFound( "/" )#request.application_url )

# Function to render image
def view_picture_view(request):
	# show a particular image
    # Get id from url
    id = int(request.matchdict['id'])
    # Get id from image
    image = Picture.get_by_id(id)
    
    # If exist any image: render
    if image:
        resp = Response( content_type="image/jpeg" )
        #resp = Response(image.category)
        resp.body = image.image
        return resp

    return Response("ERROR: photo not found")

# Function to show all images
def view_all_images_view(request):
    # Get all images
    pic = Picture.all()
    	
    return { "pictures": pic }


# START TRANSLATION FUNCTIONS (lenguage codes in ISO 639-1 (two caracters))
def trans_menu_view(request):
    # menu for translation options
    pages = Page.all()
    ids = [] # list of secondary id (language group)
    tbl = [] # table id secondary, titles and id for each language
    count = 0 # counter of pages in database (not translates of same page)
    for page in pages:
        if not page.idsec in ids:
            ids.append(page.idsec)
            tbl.append({"idsec":page.idsec,"count":count})
            for lang in langs():
                if lang == page.lang:
                    tbl[count]["title_" + page.lang] = page.title
                    tbl[count]["id_" + page.lang] = page.key().id()
                else:
                    tbl[count]["title_" + lang] = ""
                    tbl[count]["id_" + lang] = ""
            count += 1
        else:
            for i in range(len(tbl)):
                if page.idsec == tbl[i]["idsec"]:
                    tbl[i]["title_" + page.lang] = page.title
                    tbl[i]["id_" + page.lang] = page.key().id()
    for i in range(len(tbl)):
        count = 0 # counter of languages in each page
        for lang in langs():
            if tbl[i]["id_" + lang] != "":
                count += 1
                tbl[i]['last'] = lang # last language in each page
        tbl[i]['nlang'] = count # number of lenguages in each page
    return {"table":tbl,"langs":langs()}

def trans_edit_view(request):
    # edit existent translation
    if request.method=="GET":
        # first visit: show form
        id = int(request.matchdict['id'])
        p = Page.get_by_id(id)
        return {"page":p,"langs":langs(),"id":id}
    # POST form: save translation page
    id = int(request.POST.get("id"))
    p = Page.get_by_id(id)
    p.title = request.POST.get("title")
    p.text = request.POST.get("text")
    p.put() #desa a la BBDD
    return HTTPFound( "/trans_menu" )#request.application_url )

def trans_create_view(request):
    # create a new translation for a existent page
    if request.method=="GET":
        # first visit: show form
        ln = request.matchdict['ln'] # selected language
        id = int(request.matchdict['id']) # id secondary
        pages = Page.gql("WHERE idsec = :id2", id2 = id)
        exl = {} # existing languages
        for page in pages:
            exl[page.lang] = langs()[page.lang]
        return {"langs":langs(),"exl":exl,"ln":ln,"idsec":id}
    # POST form: save translation page
    idsec = int(request.POST.get("idsec"))
    lang = request.POST.get("lang")
    title = request.POST.get("title")
    text = request.POST.get("text")
    page = Page(idsec=idsec,lang=lang,title=title,text=text)
    page.put() #desa a la BBDD
    return HTTPFound( "/trans_menu" )#request.application_url )

def trans_view_view(request):
    # secondary view for trans_create_view for show translation base for create new translation
    if request.method=="GET":
        ln = request.matchdict['ln'] # selected language
        id = int(request.matchdict['id']) # id secondary
        pages = Page.gql("WHERE idsec = :id2", id2 = id)
        p = ""
        for page in pages:
            if page.lang == ln:
                p = page
                return {"page":p,"langs":langs()}

def trans_delete_view(request):
    # delete a existent translation or all translations for a page
    if request.method=="GET":
        # first visit: show form
        fn = request.matchdict['fn'] # function one (delete language page), all (delete all pages)
        id = int(request.matchdict['id']) # function one (id), function all (idsec)
        p = []
        if fn == "one":
            page = Page.get_by_id(id)
            p.append(page)
        if fn == "all":
            pages = Page.gql("WHERE idsec = :id2", id2 = id)
            for page in pages:
                p.append(page)
        return {"pages":p,"langs":langs(),"fn":fn,"id":id}
    # POST form: delete translation page or page
    fn = request.POST.get("fn")
    id = int(request.POST.get("id"))
    confirm = request.POST.get("confirm")
    if confirm == "ok":
        if fn == "one":
            page = Page.get_by_id(id)
            page.delete()
        if fn == "all":
            pages = Page.gql("WHERE idsec = :id2", id2 = id)
            for page in pages:
                page.delete()
    return HTTPFound( "/trans_menu" )#request.application_url )	

def langs():
    # change language data base to dictionary of lenguages
    #l = {}
    #lns = Langs.all()
    #for ln in lns:
    #    l[ln.code] = lns[ln.code]
    return {u"en":u"English",u"es":u"Español",u"ca":u"Català",u"fr":u"Française",u"pt":u"Português"}

def current_lang(fn="get",ln="en"):
    # get or set current lenguage
    if fn == "get":
        # ... return current lenguage
        return "en"
    if fn == "set":
        # ... set current lenguage
        return True

def translate(text):
    # translate text to a current lenguage selected from english lenguage
    pass
    # tt = Translate.gql("WHERE  en = :t", t = text)
    # return tt

# END TRANSLATION FUNCTIONS
