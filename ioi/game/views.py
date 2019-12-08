# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import django
import string
import logging
import datetime

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.conf import settings

from django.contrib.auth import logout

from random import choice

django.setup()

logger = logging.getLogger(__name__)


COOKIE_EXPIRY_TIME = datetime.datetime.now() + datetime.timedelta(days=365)


def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def home(request):
    response = render(request=request, template_name="index.html", context={})
    return response
