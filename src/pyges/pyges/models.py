# -*- coding: utf-8 -*-

from google.appengine.ext import db

# Page data base with language
class Page(db.Model):
    idsec = db.IntegerProperty()
    lang = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)

#Create Class Picture
class Picture(db.Model):
    #Picture name
    title = db.StringProperty(required=True)
    #Date creation 
    date = db.DateTimeProperty(auto_now_add=True)
    #Date last modification
    date_modify = db.DateTimeProperty(auto_now=True)
    #Image category(defined on upload mako)
    category = db.CategoryProperty(required=True)
    #Uploader
    user = db.UserProperty(required=False)
    #Image binary
    image = db.BlobProperty()

class Estils(db.Model):
	id = db.IntegerProperty(required=True)
	nom = db.StringProperty(required=True)
	contingut = db.TextProperty(required=True)

class GlobalConfig(db.Model):
    site_name = db.StringProperty()
    admin_users = db.StringListProperty()
    def admins(self):
        users = ""
        for user in self.admin_users:
            if user!="\n":
                users += user + "\n"
        return users
