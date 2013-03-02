Fork of django-registration for Django 1.5

========================
What's Different?
========================
Replaces function based views with class based views
Modifies __init__.get_version() to pass unittest expectations
Prefix test files with test_ for django-discover-runner
Drop deprecated urls.py
The docs are now incorrect, but not yet updated

Install:

settings.py:

    INSTALLED_APPS = (
    ...
    'registration',
    ...
    )

urls.py
for account email verification:

    url(r'^account/', include('registration.backends.default.urls')),

 or to create without verification:

   url(r'^account/', include('registration.backends.simple.urls')), 

To run tests, go to project root and run

    python manage.py test registration --settings=registration.tests.settings

========================
Django user registration
========================

This is a fairly simple user-registration application for Django_,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.1 or newer, but has no
other dependencies.

For installation instructions, see the file "INSTALL" in this
directory; for instructions on how to use this application, and on
what it provides, see the file "quickstart.rst" in the "docs/"
directory.