# -*- encoding: utf-8 -*-
 
from django import forms
from blog.models import Commentary
 
class AddCommentaryForm(forms.ModelForm):
  class Meta:
    model = Commentary
    fields = ('author', 'content')



class SearchForm(forms.Form):
  query = forms.CharField(min_length=3, required=False)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    phone = forms.IntegerField(required=False)
    subject = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=400,required=False,widget=forms.Textarea(attrs={'cols': 30, 'rows': 6}))
    #subject = forms.CharField(max_length=100)
    email = forms.EmailField()

