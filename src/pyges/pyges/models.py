# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Imatge(db.Model):
    titol = db.StringProperty(required=True)
    data = db.DateTimeProperty(auto_now_add=True)
    modificacio = db.DateTimeProperty(auto_now=True)
    categoria = db.CategoryProperty(required=True)
    usuari = db.UserProperty(required=False)
    imatge = db.BlobProperty()

class Page(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)

class GlobalConfig(db.Model):
    site_name = db.StringProperty()
    admin_users = db.StringListProperty()

    def admins(self):
        users = ""
        for user in self.admin_users:
            if user!="\n":
                users += user + "\n"
        return users
