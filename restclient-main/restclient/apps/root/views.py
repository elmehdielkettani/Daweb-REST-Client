from django.shortcuts import render_to_response
from django.template import RequestContext
from gaesessions import get_current_session
import logging


def view_default(request):
#    session = get_current_session()
#    logging.info("Home test 0 = %s" % session.get("url"))
#    session.set_quick("url", "leullle")
#    logging.info("Home Test 1 = %s" % session.get("url"))
    return render_to_response('root.default.html', context_instance = RequestContext(request))
