# -*- coding: utf-8 -*-

class Page:
	id = 0
	title = ""
	text = ""


def root_view(request):
    return {}

def create_page_view(request):
    return {}

def view_page_view(request):
	pagina = Page()
	pagina.id = 1234
	pagina.title = "Pàgina de prova"
	pagina.text = u"una mica de continguts...<br>\nlalalala..."

	return { "page": pagina }
