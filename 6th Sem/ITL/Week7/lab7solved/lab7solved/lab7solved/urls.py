from django.conf.urls import include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    url(r'^blog/',include('blog.urls')),
    url(r'^admin/',admin.site.urls),

]