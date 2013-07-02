# -*- encoding: utf-8 -*-
from blog.forms import SearchForm
 
def searchform(request):
  if request.method == 'GET':
    form = SearchForm(request.GET)
 
  else:
    form = SearchForm()
 
  return { 'searchform' : form }
