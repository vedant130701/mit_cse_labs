from django.conf.urls import include,url 
from blog.views import archive,create_blogpost
urlpatterns = [ 
 url(r'^$', archive, name='archive'),
 url(r'^create/', create_blogpost, name='create_blogpost'), 
 ] 
