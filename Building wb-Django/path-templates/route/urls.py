from django.urls import path
from . import views
from django.views.generic import TemplateView

# To make {% url 'route:first-view' %} work in templates
# Also, add namespace in project urls.py 
# Otherwise the name='' values will be global across all applications
app_name = 'route'  

urlpatterns = [
    path('', TemplateView.as_view(template_name='route/main.html')),
    path('first', views.FirstView.as_view(), name='first-view'), #Reference route for first as fist-view
    path('second', views.SecondView.as_view(), name='second-view'), #Name, ita  like an id
]

# References

# https://docs.djangoproject.com/en/3.0/topics/http/urls/

# https://docs.djangoproject.com/en/3.0/ref/urls/#include

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces-and-included-urlconfs
