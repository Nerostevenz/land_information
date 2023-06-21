from django.shortcuts import render, redirect
from .models import Plan, Coordinate
from django.db import IntegrityError

def add_plan(request):
    if request.method == 'POST':
        try:
            # Get data from the form
            plannumber = request.POST.get('plannumber')
            area = request.POST.get('area')
            location = request.POST.get('location')
            surveyor = request.POST.get('surveyor')
            coordinatesystem = request.POST.get('coordinatesystem')
            date = request.POST.get('date')
            num_coordinates = int(request.POST.get('num_coordinates'))

            # Create the plan object
            plan = Plan(plannumber=plannumber, area=area, location=location,
                        surveyor=surveyor, coordinatesystem=coordinatesystem, date=date)
            plan.save()

            # Create the coordinate objects
            for i in range(num_coordinates):
                pillarnumber = request.POST.getlist('pillarnumber[]')[i]
                eastings = request.POST.getlist('eastings[]')[i]
                northings = request.POST.getlist('northings[]')[i]
                coord = Coordinate(plan=plan, pillarnumber=pillarnumber,
                                   eastings=eastings, northings=northings)
                coord.save()

            return redirect('add_plan')
        except (IntegrityError, ValueError) as e:
            error_message = str(e)
            return render(request, 'add_plan.html', {'error_message': error_message})

    return render(request, 'add_plan.html')


# views.py

from django.shortcuts import render
from .models import Coordinate
from django.contrib import messages

def query_plan(request):
    if request.method == 'POST':
        # Get pillarnumber from the form
        pillarnumber = request.POST.get('pillarnumber')

        # Query the database
        coords = Coordinate.objects.filter(pillarnumber=pillarnumber)

        if coords.exists():
            # Get the plan associated with the coordinates
            plan = coords.first().plan

            return render(request, 'query_result.html', {'plan': plan, 'coords': coords})
        else:
            # If no coordinates are found, add a message to the user
            messages.error(request, 'There is no pillar number with that number.')
    
    return render(request, 'query_plan.html')




def query_result(request):
    pillarnumber = request.GET.get('pillarnumber')
    coordinates = Coordinate.objects.filter(pillarnumber=pillarnumber)
    context = {'coordinates': coordinates}
    return render(request, 'query_result.html', context)

def home(request):
    return render(request, 'home.html')
