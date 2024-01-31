#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if items == search else items for items in my_list]
