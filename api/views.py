from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from tcp.models import *
from .serializers import *
from datetime import datetime
from pytz import UTC


@api_view(['GET'])
@permission_classes((AllowAny,))
# Create your views here.
def query_location(request):
    '''
    Query location information through HTTP get.
    GET /api/location/latest/  --Default: Return the last record.
    GET /api/location/range/yyyy/mm/dd/HH/MM/SS/yyyy/mm/dd/HH/MM/SS  --Return records in the time range.
    :param request: HTTP request.
    :return:
    '''
    # Analysis incoming request path.
    path = request.path.encode('utf-8')
    # Decode to string.
    path = path.decode('utf-8')
    # Cut the first and last char.
    path = path[1:]
    # Split
    path_split = path.split('/')
    print(path_split)
    # Do query.
    if path_split[2] == '' or path_split[2] == 'latest':
        location_list = Location.objects.last()
        location_serializer = LocationSerializer(location_list)
        return Response(location_serializer.data, status=200)
    elif path_split[2] == 'range':
        start_dt = datetime(int(path_split[3]), int(path_split[4]), int(path_split[5]), int(path_split[6]),
                            int(path_split[7]), int(path_split[8]))
        start_dt = start_dt.replace(tzinfo=UTC)
        end_dt = datetime(int(path_split[9]), int(path_split[10]), int(path_split[11]), int(path_split[12]),
                          int(path_split[13]), int(path_split[14]))
        end_dt = end_dt.replace(tzinfo=UTC)
        location_list = Location.objects.filter(time__range=[start_dt, end_dt])
        location_serializer = LocationSerializer(location_list, many=True)
        return Response(location_serializer.data, status=200)
    else:
        return HttpResponse(status=404)


@api_view(['GET'])
@permission_classes((AllowAny,))
# Create your views here.
def query_alarm_status(request):
    '''
    Query alarm status information through HTTP get.
    GET /api/status/latest/  --Default: Return the last record.
    GET /api/status/range/yyyy/mm/dd/HH/MM/SS/yyyy/mm/dd/HH/MM/SS  --Return records in the time range.
    :param request: HTTP request.
    :return:
    '''
    # Analysis incoming request path.
    path = request.path.encode('utf-8')
    # Decode to string.
    path = path.decode('utf-8')
    # Cut the first and last char.
    path = path[1:]
    # Split
    path_split = path.split('/')
    print(path_split)
    # Do query.
    if path_split[2] == '' or path_split[2] == 'latest':
        alarm_status_list = Alarm.objects.last()
        alarm_status_serializer = AlarmStatusSerializer(alarm_status_list)
        return Response(alarm_status_serializer.data, status=200)
    elif path_split[2] == 'range':
        start_dt = datetime(int(path_split[3]), int(path_split[4]), int(path_split[5]), int(path_split[6]),
                            int(path_split[7]), int(path_split[8]))
        start_dt = start_dt.replace(tzinfo=UTC)
        end_dt = datetime(int(path_split[9]), int(path_split[10]), int(path_split[11]), int(path_split[12]),
                          int(path_split[13]), int(path_split[14]))
        end_dt = end_dt.replace(tzinfo=UTC)
        alarm_status_list = Alarm.objects.filter(time__range=[start_dt, end_dt])
        alarm_status_serializer = AlarmStatusSerializer(alarm_status_list, many=True)
        return Response(alarm_status_serializer.data, status=200)
    else:
        return HttpResponse(status=404)