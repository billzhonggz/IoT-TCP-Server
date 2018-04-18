from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import RawData, ServerOperation


# Create your views here.

def index(request):
    server_records = ServerOperation.objects.order_by('status_change_date_time')[:5]
    server_log = RawData.objects.order_by('receive_date_time')[:5]
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
        ServerOperation.run_tcp_server(ServerOperation)
        return render(request, 'tcp/index.html', {
            'message': 'TCP start up request sent.',
        })
    elif choice == 'off':
        ServerOperation.stop_tcp_server(ServerOperation)
        return render(request, 'tcp/index.html', {
            'message': 'TCP terminate request sent.',
        })
    else:
        return render(request, 'tcp/index.html', {
            'message': 'You didn\'t select any operation.',
        })
