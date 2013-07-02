# -*- encoding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from blog.models import Post
from blog.forms import AddCommentaryForm, SearchForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from django.shortcuts import render_to_response
from django.core.mail import send_mail


##General purpose
import datetime

##Owner
import func_calendar

##Should be in func_calendar, but i dont want to instanciate twice Django Models
def my_generated_calendar():
	#PickUp days that have been blogged
        days = []
	now = datetime.datetime.now()
        post_dates = Post.objects.filter(publication_date__year=now.year,publication_date__month=now.month)
        for item in post_dates:
            if item.publication_date.day not in days:
                days.append(item.publication_date.day)
	#format that days in html
	myhtml= func_calendar.createCal(now.year,now.month,now.day,days)
	return myhtml
##Should be in func_calendar, but i dont want to instanciate twice Django Models
 
class PostList(ListView):
    template_name = 'postlist.html'
    context_object_name = 'post'
    paginate_by = 2
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['recent'] = Post.objects.all()[:3]
        context['my_calendar'] = my_generated_calendar()
        return context

class PostDetails(TemplateView):
  template_name = 'postdetails.html'
 
  def post(self, request, *args, **kwargs):
    return self.get(request, *args, **kwargs)
 
  # Overriding
  def get_context_data(self, **kwargs):
    context = super(PostDetails, self).get_context_data(**kwargs)
    context['recent'] = Post.objects.all()[:3]
    context['my_calendar'] = my_generated_calendar()
 
    post = self.get_post(kwargs['slug'])
    form = self.get_form(post)
 
    context.update({'form':form, 'post':post})
 
    return context
 
  # Helper
  def get_post(self, slug):
    return Post.objects.get(pk=slug)
 
  # Helper
  def get_form(self, post):
    if self.request.method == 'POST':
      form = AddCommentaryForm(self.request.POST)
      if form.is_valid():
        commentary = form.save(commit=False)
        post.commentary_set.add(commentary)
      else:
        return form
 
    return AddCommentaryForm()



class SearchResults(ListView):
  template_name = "searchresults.html"
 
  # Override
  def get_queryset(self):
    from django.db.models import Q
    if self.request.method == 'GET':
      form = SearchForm(self.request.GET)
      if form.is_valid():
        query = form.cleaned_data['query']
        words = query.split(' ')
        qobjects = [Q(content__icontains=w) | Q(title__icontains=w) for w in words]
        condition = reduce(lambda x,y: x & y, qobjects)
        results = Post.objects.filter(condition)
        return results
 
    return Post.objects.none()


##TODO:Probably both views, could be implemented together... look for it
def ArchiveYear(request,year):
    results = Post.objects.filter(publication_date__year=year)
    return render_to_response('archiveresults.html',
                                                RequestContext(request,{'results':results,}))

def ArchiveMonth(request,year,month):
    results = Post.objects.filter(publication_date__year=year,publication_date__month=month)
    return render_to_response('archiveresults.html',
                                                RequestContext(request,{'results':results,}))                
def about(request):
    recent = Post.objects.all()[:3]
    my_calendar = my_generated_calendar()

    return render_to_response('about.html',RequestContext(request,{
                                            'recent':recent,
                                            'my_calendar':my_calendar,
						}))


def contact(request):
    correo_enviado=''

    recent = Post.objects.all()[:3]
    my_calendar = my_generated_calendar()
    try:
        my_contactform = ContactForm()
    except:
        my_contactform = ContactForm()


    if request.method == 'POST': # If the form has been submitted...
        contactform = ContactForm(request.POST) # A form bound to the POST data
        if contactform.is_valid():
            name = contactform.cleaned_data['name']
            surname = contactform.cleaned_data['surname']
            phone = str(contactform.cleaned_data['phone'])
            subject = contactform.cleaned_data['subject']
            comment = contactform.cleaned_data['comment']
            email = [contactform.cleaned_data['email']]
            email = ['bvcelari@gmail.com']
            email_text = str(contactform.cleaned_data['email'])
            sender = 'webmaster@bvcelari.com'
            message = ' Nombre:' + name + '\n Apellido:' + surname + '\n Telefono:' + phone + '\n Email: ' + email_text +'\n Consulta:' + comment
            correo_enviado = u'Su correo ha sido enviado, tan pronto...'
            #cc_myself = contactform.cleaned_data['cc_myself']
            #if cc_myself:
            #    recipients = recipients + ';' +cc_myself
	    print "SUBJECT:",subject," \nMESSAGE", message,"\n SENDER ", sender, "\n EMAIL", email
            send_mail(subject, message, sender, email,fail_silently=False)


    return render_to_response('contact.html',

						RequestContext(request, 
						{
					    'recent':recent,
					    'my_calendar':my_calendar,
                                            'my_contactform':my_contactform,
                                            'correo_enviado':correo_enviado
                                            })
)

