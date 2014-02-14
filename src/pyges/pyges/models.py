# -*- coding: utf-8 -*-

from google.appengine.ext import db

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
