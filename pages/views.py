# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Node, ImageNode

image_tree = ImageNode()

# Create your views here.
def index(request):
    nodes = Node.objects.all()
    for n in nodes:
        s = n.name
        levels = list(map(lambda p: p.strip(), s.split(">")))
        image_tree.add(levels,n.size)
        # print(levels)
    image_tree.print_tree()
    return render(request, 'index.html', {'nodes': nodes})