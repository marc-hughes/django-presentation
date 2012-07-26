from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings

import twitter


from models import InterestingPerson

import logging

logger = logging.getLogger(__name__)

def homepage(request):
    return render_to_response('demoapp/homepage.html', context_instance=RequestContext(request))

def people(request):
    people = InterestingPerson.objects.all().order_by("id")
    return render_to_response('demoapp/people.html', {'people':people, 'user':request.user}, context_instance=RequestContext(request))
    
def follow(request, person_id):
    person = get_object_or_404(InterestingPerson, id=person_id)

    tokens = request.user.social_auth.get(provider="twitter").tokens
    access_token_secret = tokens['oauth_token_secret']
    access_token_key = tokens['oauth_token']

    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, 
                      consumer_secret=settings.TWITTER_CONSUMER_SECRET, 
                      access_token_key=access_token_key, 
                      access_token_secret=access_token_secret)
    api.CreateFriendship(person.twitter_username)
    
    person.follow_count += 1
    person.save()
    
    return HttpResponseRedirect(reverse("people"))
    
