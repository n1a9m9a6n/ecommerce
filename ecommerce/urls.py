
from django.contrib import admin
from django.urls import path, include
#from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path("", include('ecom.urls')),
	path("", include('siteadmin.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
