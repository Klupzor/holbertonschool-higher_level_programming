#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = my_list.copy()
    li.insert(li.index(search), replace)
    li.remove(search)
    return li
