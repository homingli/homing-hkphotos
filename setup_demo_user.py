#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth import authenticate

# Create our own demo user automatically.
try:
    auth_models.User.objects.get(username='demo')
except auth_models.User.DoesNotExist:
    print '*' * 80
    print 'Creating demo user -- login: demo, password: demo'
    print '*' * 80
    assert auth_models.User.objects.create_superuser('demo', 'demo@as.com', 'demo')
else:
    print 'Demo user already exists.'

# Test authentication
print '*' * 80
print 'Testing demo user authentication.'
print '*' * 80
user = authenticate(username='demo', password='demo')
if user is not None:
    if user.is_active:
        print("Demo user is active!")
    if user.is_staff:
        print("Demo user is staff!")
    if user.is_superuser:
        print("Demo user is superuser!")
else:
    print("username and password were incorrect.")
