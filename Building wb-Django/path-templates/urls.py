from django.urls import path
from . import views #from parent package
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='views'
urlpatterns = [ 
    # pre-defined class from Django
    path('', TemplateView.as_view(template_name='views/main.html')),
    # function from views.py
    path('funky', views.funky), #Just the HTML Response
    path('danger', views.danger), #commands can be passed
    path('game', views.game), #escape
    path('rest/<int:guess>', views.rest),  #django documentation,  stands for 
                                           #the parameter after the rest has to be an integer(NUMBER)
    # Play with redirect
    path('bounce', views.bounce), #Redirecting.
    # our class from views.py
    path('main', views.MainView.as_view()), #class based view, allows to have or not a method for the view.
                                            #as_view because the MainView is a class and not a function
    path('remain/<slug:guess>', views.RestMainView.as_view()), #with the <slug:guess> after the remain would mean
                                                               #that as another parameter for the class is the string: guess PARSED
]

