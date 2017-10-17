# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# from queue import Queue

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

class ImageNode(object):
    """Data structure to hold the tree scraped from imagenet data
    
    Attributes:
        name: A string representing the customer's name.
        size: A float tracking the current balance of the customer's account.
        children: A float tracking the current balance of the customer's account.
    """
    def __init__(self):
        self.name = ""
        self.size = 0
        self.children = []
    
    def __str__(self):
        return "{{ name: '{0}', size: {1}, children: {2} }}".format(self.name, self.size, self.children)
    
    def print_tree(self):
        print("** START PRINT_TREE **")
        s = ""
        q = []
        q.append(self)
        while(len(q) > 0):
            t = q.pop()
            print(t)
            for c in t.children:
                print("Children are :")
                q.append(c)
        print("** END PRINT_TREE **")
        
    def add(self,path_arr,size):
        print("Adding ({0},{1})".format(path_arr, size))
        if(len(path_arr) == 1):
            print("This is the leaf node")
            self.name = path_arr[0]
            self.size = size
        elif(len(path_arr) > 0): # Path has at least one non-leaf node. Current min size is 2
            # print("Path has some value")
            if(len(self.name) < 1): # No data in the current sub-tree yet and this is not the leaf node in the path
                self.name = path_arr[0]
                child = ImageNode()
                self.children += child
                child.add(path_arr[1:], size)       
            else: # Tree has existing data
                curr_node = path_arr[0]
                if(curr_node == self.name):
                    print("Same node detected")
                elif(curr_node in self.children):
                    print("Child of current node detedted")
                else:
                    print("new child detected {0} of {1}".format(curr_node, self.name))
                # print("Tree has existing data")        
        