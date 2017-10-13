# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Node

# Create your views here.
def index(request):
    nodes = Node.objects.all()
    return render(request, 'index.html', {'nodes': nodes})
