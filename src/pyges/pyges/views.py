# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound
from google.appengine.api import users


def root_view(request):
    p = Page.all() 
    return { "pages":p }
                 

def create_page_view(request):
    
    user = users.get_current_user()
    if not user:
        return HTTPFound (users.create_login_url())
    else:
        return { "user": user }
        title = request.POST.get("title")
        if not title:
    	# 1st visit: show form
            return {}
        else:
    # filled form: save page
            text = request.POST.get("text")
            page = Page(title=title,text=text)
            page.put()
    
    
            return HTTPFound( "/" )#request.application_url )



def view_page_view(request):
	# show a particular page
    id = int(request.matchdict['id'])
    p = Page.get_by_id(id)
    return { "page": p }













