import webapp2
import jinja2
import random
import os
# from model import Character
# from model import User
# from google.appengine.api import users
# from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = False)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('html/Homepage.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        # chars_fetch = Character.query().fetch()
        # if(chars_fetch==[]):
        #     putChars()
        login_template = jinja_environment.get_template('html/Test.html')
        user = users.get_current_user()
        print(user)
        user_query = User.query()
        user_fetch = user_query.fetch()
