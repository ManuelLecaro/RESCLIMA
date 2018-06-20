from django.shortcuts import render
from django.http import HttpResponseRedirect
from TimeSeries.forms import *
from parsers.csv_parsers_module import *
from django.contrib import messages
from models import StationType, Station;
from django.contrib.gis.geos import Point


def show_options(request):
  return render(request,"home_series.html")


def addSensor(data):
    try:
        stationType_id = int(data["stationType"]);
        serialNum = data["serialNum"];
        latitude = float(data["latitude"]);
        longitude = float(data["longitude"]);
        frequency = data["frequency"];
        token = data["token"];

        stationType = StationType.objects.get(id=stationType_id);
        automatic = stationType.automatic;
        station = Station();
        station.serialNum = serialNum;
        station.location = Point(longitude,latitude);
        station.active = True;
        station.stationType = stationType;

        if(automatic==True):
            if(frequency=="" or token == ""):
                return "Error: faltan argumentos";
            station.frecuency = float(frequency);
            station.token = token;

        station.save();
    except Exception as e:
        return "Error " + str(e)

    return None

def new_sensor(request):
    
    if request.method == "GET":
        station_types = StationType.objects.all()
        options = {'station_types':station_types}
        return render(request, 'new_sensor.html',options)
    elif request.method == "POST":
        err_msg = None;
        form = StationForm(request.POST)
        if form.is_valid():
            err_msg = addSensor(request.POST);
        else:
            err_msg = form.errors

        if(err_msg==None):
            return HttpResponseRedirect("/series")
        else:
            station_types = StationType.objects.all()
            options = {'station_types':station_types,"err_msg":err_msg}
            return render(request, 'new_sensor.html',options)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            station_type = form.cleaned_data['select']
            file = request.FILES['file']
            if(station_type == "HOBO-MX2300"):
                try:
                    result = parseHOBO(file)
                    messages.success(request, 'Successfully saved')
                except KeyError:
                    messages.error(request, 'Could not save the file.', extra_tags='alert')
    elif request.method == "GET":
        form = UploadFileForm()
        return render(request, 'base_form.html', {'form': form})
