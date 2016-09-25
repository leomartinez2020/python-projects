import cgi
from google.appengine.api import users
import webapp2
from random import shuffle
MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body><h2>The scrambled sentence is: </h2><pre>')
        m = cgi.escape(self.request.get('content'))
        k = m.split()
        shuffle(k)
        k = ' '.join(k)
        self.response.write(k)
        #self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre><br>')
        self.response.write('</body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
