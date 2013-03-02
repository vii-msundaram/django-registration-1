"""
URLconf for registration and activation, using django-registration's
one-step backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.simple.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls import *

from django.views.generic import TemplateView

from registration.views import ActivateView, RegisterView


urlpatterns = patterns('',
  url(r'^register/$',
    RegisterView.as_view(),
    {'backend': 'registration.backends.simple.SimpleBackend'},
    name='registration_register'),
  url(r'^register/closed/$',
    TemplateView.as_view(
    template_name='registration/registration_closed.html'),
    name='registration_disallowed'),
  (r'', include('registration.auth_urls')),
)
