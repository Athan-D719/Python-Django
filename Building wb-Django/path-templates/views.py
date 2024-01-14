from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape  #Doesn't interpret the HTML entities  SAFE.
from django.views import View
#THE REQUEST OBJECT WOULD BE IN THE TEMPLATES AS EX https://.../views/funky as the href='funky'
# in the urls.py will redirect it as the function with the path(funky, views.funky) importing the function from views.py
# Create your views here.
def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)
                      #since the requests changes from  = https://...path-templates/main.html TO https://.../views/danger?guess=42
def danger(request) : #since its a dictionary we can get the response values as = request.GET['guess']
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p> 
    </body></html>"""
    return HttpResponse(response)

def game(request) : #The safer version since it will not take the cahracters as an HTML decoded, but the string itself.
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)

def rest(request, guess) : #not having to tear the parameters.
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>  
    </body></html>"""
    return HttpResponse(response)

# This is a command to the browser
def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm') #Header HttoResponseRedirect('URL')
    #2 Responses, the 302 -> 200 and a 404 in case there is no favicon

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/
class MainView(View) : #Class based view, 
    def get(self, request): #Just retrieving a HTTP response and we can extract the parameters of the request
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

class RestMainView(View) :
    def get(self, request, guess): #request and guess parameters
        print("We got a slug from the URL",guess); #already the value we wanted
        response = """<html><body>
        <p>Your guess was """+escape(guess)+"""</p> 
        </body></html>"""
        return HttpResponse(response)

