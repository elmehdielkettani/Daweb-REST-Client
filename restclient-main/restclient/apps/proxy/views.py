import urllib2
import re
import logging
from urllib2 import HTTPError
from django.http import HttpResponse
from django.utils import simplejson


def call_proxy(httpRequest):  
    url = httpRequest.GET["link"]
    if not url.startswith("http://"):
        url = "http://%s" % url

    if "urls" in httpRequest.session:
        urls = httpRequest.session["urls"]
        urls.append(url)
        httpRequest.session["urls"] = urls
    else:
        httpRequest.session["urls"] = [url]


    regex = re.compile('^HTTP_')
    requestHeaders = dict((regex.sub('', header), value) for (header, value) in httpRequest.META.items() if header.startswith('HTTP_'))
    
    req = urllib2.Request(url, None, requestHeaders)
    
    try:
        resp = urllib2.urlopen(req)
        content = resp.read()
        statusCode = resp.code
        response = HttpResponse(content, status=statusCode)
        for k, v in resp.info().items():
            logging.info("%s ---> %s" % (k,v))
            response[k]=v
    except HTTPError, e:
        content = e.read()
        statusCode = e.code
        response = HttpResponse(content, status=statusCode)
        for k, v in e.info().items():
            response[k]=v
    except Exception, e:
        response = HttpResponse(status=404)

    logging.info(response.status_code)
    return response

def autocomplete_urls(httpRequest):

    if "urls" in httpRequest.session:
        return HttpResponse("{ source: %s }" % simplejson.dumps(httpRequest.session["urls"]), status=200)
    else:
        return HttpResponse(None, status=200)