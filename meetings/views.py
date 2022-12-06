from django.shortcuts import render
from .forms import CalendarForm

def calendar_view(request):
    context = {}
    form = CalendarForm()
    context['form'] = form
    if request.GET:
        temp = request.GET['cal_field']
        print(type(temp))
    return render( request, 'meetings/calendar.html', context)



