from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

def index(request,type,year):
    year = int(year)
    type = int(type)
    if year < 1900 or year > 2099: year = date.today().year
    title = "MyClub Event Calendar - %s" % (year)
    cal = HTMLCalendar().formatyear(year)
    if type == 1:
    #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
        return render(request, 'basic.html', {'title': title, 'cal': cal})
    elif type == 2:
        return render(request, 'basic2.html', {})