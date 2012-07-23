from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

def direct_to_template(request, slide):
    return render_to_response('presentation/slide%s.html' % slide, {"slidenum":int(slide)}, context_instance=RequestContext(request))
    try:
        return render_to_response('presentation/slide%s.html' % slide, {"slidenum":int(slide)}, context_instance=RequestContext(request))
    except:
        return redirect(reverse("slide", kwargs={'slide':'1'}))