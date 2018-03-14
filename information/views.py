from django.shortcuts import render
from .models import Districts, Divisions
# Create your views here.


def DistrictList(request):
    districts = Districts.objects.all()

    # if you wanna only specific place that you have visited, more than specific education
    #  rate equal or greater than and you can see also definite division's districts.
    #districts = Districts.objects.filter(visited=True)
    #districts = Districts.objects.filter(education_rate__gt=40 )
    #districts = Districts.objects.filter(education_rate__gte=50 )
    #districts = Districts.objects.filter(education_rate__lt=60 )
    #Districts.objects.filter(education_rate__lte=50)
    #districts = Districts.objects.filter(division__name='Khulna')
    #div = Divisions.objects.get(name='Khulna')
    #districts = Districts.objects.filter(division=div)

    context = {
        'districts': districts,
    }
    return render(request, 'info/districts.html', context)

def DivisionList(request):
    divisions = Divisions.objects.all()
    context = {
        'divisions': divisions,
    }
    return render(request, 'info/divisions.html', context)

def DistsOfDivs(request):
    #divisions = Divisions.objects.get(pk=divs_id)
    divisions = Divisions.objects.all()
    districts = Districts.objects.filter(division=divisions[0])
    context = {
        'division': divisions,
        'districts': districts,
    }

    return render(request, 'info/dists-divs.html', context)
