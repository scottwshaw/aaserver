import cgi
from django.utils import simplejson
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from yaml import load

class JSONHandler(webapp.RequestHandler):
    def get(self):
        filename = "data/" + self.request.path + ".yml"
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(simplejson.dumps(load(open(filename,'r'))))

application = webapp.WSGIApplication(
                                     [('/speakers', JSONHandler),
                                      ('/topics', JSONHandler)],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
