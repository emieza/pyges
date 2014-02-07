# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Page(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)

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
