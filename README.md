# drfrequests
Django Rest Framework Requests


### Test Build

* increment the version number in your `setup.cfg` file
* `$ python3 -m build`
* First upload to TestPypi: ``twine upload --repository testpypi dist/*`
* install `pip install --index-url https://test.pypi.org/simple/ --no-deps drfrequests`
