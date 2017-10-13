# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Node(models.Model):
    # author = models.ForeignKey('auth.User')
    # title = models.CharField(max_length=200)
    name = models.TextField()
    size = models.BigIntegerField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return "{{name: '{0}', size: {1}}}".format(self.name, self.size)
        