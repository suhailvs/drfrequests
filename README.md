# drfrequests

Django Rest Framework Requests

[Documentation](http://drfdocs.com)

### Installation

Install using pip:

    pip install drfrequests

Add 'rest_framework_docs' to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = [
        ...
        'rest_framework_requests',
    ]

Finally include the `rest_framework_docs` urls in your `urls.py`:

    urlpatterns = [
        ...
        path('docs/', include('rest_framework_requests.urls')),
    ]


### Settings
You can find detailed information about the package's settings at [the docs](http://drfdocs.com/settings/).

    REST_FRAMEWORK_DOCS = {
        'HIDE_DOCS': True  # Default: False
    }


### Credits

This project is a frok of <https://github.com/manosim/django-rest-framework-docs> which is a fork of <https://github.com/marcgibbons/django-rest-framework-docs>


### Test Build

* increment the version number in your `setup.cfg` file
* `$ python3 -m build`
* First upload to TestPypi: `twine upload --repository testpypi dist/*`
* install `pip install --index-url https://test.pypi.org/simple/ --no-deps drfrequests`

