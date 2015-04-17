# media-table
This project is about a small Ikea-like table that has a 15" monitor built in. This monitor is controlled by a raspberry pi to change color, set a picture, etc. via a webinterface. Uses the python-django framework.

## Installation

### Requirements

First of all you need a working python 2.7 installation. Afterwards you have to install [`django`](https://pypi.python.org/pypi/Django/), [`django-widget-tweaks`](https://pypi.python.org/pypi/django-widget-tweaks/), [`django-bootstrap3`](https://pypi.python.org/pypi/django-bootstrap3), [`django-admin-bootstrapped`](https://pypi.python.org/pypi/django-admin-bootstrapped/), [`webcolors`](https://pypi.python.org/pypi/webcolors/) and [`pyzmq`](https://pypi.python.org/pypi/pyzmq/).

```
sudo pip install django django-widget-tweaks django-bootstrap3 django-admin-bootstrapped webcolors pyzmq
```

### Installation Instructions

Afterwards you can build the database and run a test server.

```
python manage.py makemigrations
python manage.py syncdb
python manage.py runserver 0.0.0.0:8000
```

And for the client

```
python client.py
```

For further information on how to deploy a django application see [the official documentation](https://docs.djangoproject.com/en/1.8/howto/deployment/).