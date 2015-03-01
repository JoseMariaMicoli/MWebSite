# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.views import generic
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import FormContato
from django.template import RequestContext, Context
from django import forms as forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.core.context_processors import csrf

def contactview(request):
    subject = request.POST.get('assunto', '')
    message = request.POST.get('mensagem', '')
    from_email = request.POST.get('email', '')

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['josemaria.micoli@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('contato/thankyou/')
    else:
        return render_to_response('contact.html', {'form': FormContato()}, RequestContext(request))
    
    return render_to_response('contact.html', {'form': FormContato()}, RequestContext(request))


def thankyou(request):
    return render_to_response('thankyou.html')

def sobre(request):
    return render_to_response('about.html')

# Create your views here.
class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
