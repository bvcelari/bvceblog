# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import auth
 
class Post(models.Model):
 
  title = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255,blank=True)
  machine_name = models.SlugField(max_length=255, primary_key=True)
  content = models.TextField(blank=True)
  publication_date = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(auth.models.User)
 
  def __unicode__(self):
    return self.title
 
  def excerpt(self):
    return self.content[:300] + u'…'

  def get_absolute_url(self):
    from django.core.urlresolvers import reverse
    return reverse('postdetails',kwargs={ 'slug':self.machine_name })
 
  class Meta:
    ordering = [u'-publication_date']



class Commentary(models.Model):
  post = models.ForeignKey(Post)
  content = models.TextField()
  publication_date = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=50, default=u'Uno que viene y dice... ')
  #should add a valid email address.. .and confirm by admin before show, should add an automated email too :o)
 
  def __unicode__(self):
    return self.author + u'@' + unicode(self.post)
    #return self.owner + u'@' + unicode(self.post)
 
  class Meta:
    verbose_name_plural = u'commentaries'
    ordering = [u'-publication_date']
