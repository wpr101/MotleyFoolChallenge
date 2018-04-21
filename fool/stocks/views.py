# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
import json

def index(request):
    with open("./stocks/quotes_data.json", encoding='utf-8') as json_data:
        data = json.load(json_data)

    #return HttpResponse(template.render('index.html'))
    return render(request, 'stocks/index.html', {})
    #return render_to_response('fool/index.html')
