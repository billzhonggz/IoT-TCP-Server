from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import RawData, ServerOperation, run_tcp_server, stop_tcp_server


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


def operation(request):
    choice = request.POST['choice']
    if choice == 'on':
        # TODO: After TCP server started, statements followed will be sucked.
        run_tcp_server()
        return render(request, 'tcp/index.html', {
            'message': 'TCP start up request sent.',
        })
    elif choice == 'off':
        stop_tcp_server()
        return render(request, 'tcp/index.html', {
            'message': 'TCP terminate request sent.',
        })
    else:
        return render(request, 'tcp/index.html', {
            'message': 'You didn\'t select any operation.',
        })
