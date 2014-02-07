# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Picture(db.Model):
    title = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)
    date_modify = db.DateTimeProperty(auto_now=True)
    category = db.CategoryProperty(required=True)
    user = db.UserProperty(required=False)
    image = db.BlobProperty()

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
