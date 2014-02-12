# -*- coding: utf-8 -*-


from models import *
from pyramid.httpexceptions import HTTPFound
# Import class response(pyramid)
from pyramid.response import Response

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
    return HTTPFound( "/" ) #request.application_url )

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






