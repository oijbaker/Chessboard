from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	path(
		"favicon.ico",
		RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
	),
	path('he', views.hello_world, name='hello_world'),
	path('fib', views.create_fib, name='create_fib'),
	path('', views.test_api, name='test_api'),
]
