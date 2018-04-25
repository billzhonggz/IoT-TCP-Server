from django.http import HttpResponse
from django.template import loader

from .models import RawData, ServerOperation


# Create your views here.

def index(request):
    server_records = ServerOperation.objects.order_by('status_change_date_time')
    server_log = RawData.objects.order_by('receive_date_time')
    template = loader.get_template('tcp/index.html')
    context = {
        'server_records': server_records,
        'server_log': server_log,
    }
    return HttpResponse(template.render(context, request))