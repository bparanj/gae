from google.appengine.api import users
import webapp2
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        time = datetime.datetime.now()
        user = users.get_current_user()
        
        if not user:
            navbar = ('<p>Welcome! <a href="%s">Sign in or register</a> to customize.</p>' % 
            (users.create_login_url(self.request.path)))
        else:
            navbar = ('<p>Welcome, %s! You can <a href="%s">sign out</a>.</p>'
                        % (user.email(), users.create_logout_url(self.request.path)))

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('''
        <html>
          <head>
              <title>The time is...</title>
          </head>
          <body>
          %s
          <p>The time is: %s</p>
          </body>
         </html>''' % (navbar, str(time)))
        
app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
