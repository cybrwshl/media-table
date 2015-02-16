# media-table
This project is about a small Ikea-like table that has a 15" monitor built in. This monitor is controlled by a raspberry pi to change color, set a picture, etc. via a webinterface. Uses the python-django framework.

## Installation

### Requirements

First of all you need a working python 3.4 installation. Afterwards you have to install [`django`](https://pypi.python.org/pypi/Django/), [`django-widget-tweaks`](https://pypi.python.org/pypi/django-widget-tweaks/), [`django-bootstrap3`](https://pypi.python.org/pypi/django-bootstrap3) and [`django-admin-bootstrapped`](https://pypi.python.org/pypi/django-admin-bootstrapped/).

```
pip install django django-widget-tweaks django-bootstrap3 django-admin-bootstrapped
```

### Installation Instructions

Afterwards you can build the database and run a test server.

```
python manage.py makemigrations
python manage.py syncdb
python manage.py runserver
```

For further information on how to deploy a django application see [the official documentation](https://docs.djangoproject.com/en/1.7/howto/deployment/).