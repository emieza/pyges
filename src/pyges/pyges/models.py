# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Page(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
