from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def DisplayTcpReceive(request):
    now = datetime.datetime.now()
    html = "<html><body>Current time is %s. </body></html>" % now
    # TODO: Set response as a template, insert the received data.
    return HttpResponse(html)