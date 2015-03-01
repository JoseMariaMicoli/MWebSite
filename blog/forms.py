# -*- coding:utf-8 -*-
from django import forms
from localflavor.br.forms import *
   
class FormContato(forms.Form):
    nome = forms.CharField()
    assunto = forms.CharField()
    email = forms.EmailField(label=u'E-mail')
    cidade = forms.CharField()
    estado = forms.ChoiceField(choices=STATE_CHOICES)
    mensagem = forms.CharField(widget=forms.Textarea())

