# -*- coding: utf-8 -*-

from models import *
from pyramid.httpexceptions import HTTPFound

def root_view(request):
	# show all pages
    p = Page.all()
    return { "pages":p }

def create_page_view(request):
    title = request.POST.get("title")
    if not title:
    	# 1st visit: show form
        return {}
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
