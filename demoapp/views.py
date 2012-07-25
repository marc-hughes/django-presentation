from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from models import InterestingPerson

def homepage(request):
    return render_to_response('demoapp/homepage.html', context_instance=RequestContext(request))

def people(request):
    people = InterestingPerson.objects.all()
    return render_to_response('demoapp/people.html', {'people':people}, context_instance=RequestContext(request))
    
def person(request, person_id):
    pass
