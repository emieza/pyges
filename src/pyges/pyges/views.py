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
    return { "pages":p, "pictures": pic }


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
     except:
	return {'missatge':'Omple tots els camps'}
     message_body = "<h3>"+ fname + " " + sname + "</h3><h5>" + email + "</h5>" + msg
     mail.send_mail(
     sender='sundavar.l2@gmail.com',
     to='sundavar.l2@gmail.com',
     subject='Prueba enviar mail',
     body=fname+" "+sname+" "+email+" "+msg,     
     html=message_body)
     return{'missatge':'Misatge enviat'}


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
		return { "page": p , "pages":b, "contingut":last.lastskin, "listskins":e}
	else:
		# show a particular page
		e = Estils.all()
		id = int(request.matchdict['id'])
		p = Page.get_by_id(id)
		b = Page.all()
		return { "page": p , "pages":b, "listskins":e, "contingut":last.lastskin}


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






