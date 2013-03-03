Fork of django-registration for Django 1.5

What's Different?
-----------------------
* Replaces function based views with class based views
* Modifies \_\_init\_\_.get_version() to pass unittest expectations
* Prefix test files with test_ for django-discover-runner
* The docs are now incorrect, but not yet updated.
* Ability to restrict accounts to 1/email address
    * Disabled by default. Uncomment clean_email in registration/forms.py to use
    * If disabled, password reset emails will be sent to all accounts using the reset email address


Install:
-----------------------

Include registration directory in your project directory, then update:

###settings.py:

    INSTALLED_APPS = (
        ...
        'registration',
        ...
    )

###urls.py
for account email verification:

    url(r'^account/', include('registration.backends.default.urls')),

 or to create without verification:

    url(r'^account/', include('registration.backends.simple.urls')), 

###site_fixture.json
Update domain and name with the correct fields, then call:
	
	python manage.py loaddata registration/fixtures/site_fixture.json

Alternatively, open the /admin panel and manually edit the data

To run tests, go to project root and run

    python manage.py test registration --settings=registration.tests.settings


Django user registration
-----------------------

This is a fairly simple user-registration application for Django_,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django <del>1.1</del> 1.5 or newer, but has no
other dependencies.
