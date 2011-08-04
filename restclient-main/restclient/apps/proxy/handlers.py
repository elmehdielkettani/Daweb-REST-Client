from urllib2 import HTTPError
import urllib2




class ProxyRequestHandler(RequestHandler):
    '''
    Handles requests to the main website.
    '''

    def __init__(self, httpRequest):
        if(httpRequest.method == 'GET'):
            req = urllib2.Request(httpRequest.build_absolute_uri(httpRequest.get_full_path()), None, httpRequest.META)
        try:
            resp = urllib2.urlopen(req)
            content = resp.read()
            status = resp.code
            response =  HttpResponse(content, status_code= status)
            for k, v in resp.info():
                setattr(response, k, v)
        except HTTPError, e:
            content = e.read()
            status = e.code
            response =  HttpResponse(content, status_code= status)
            for k, v in e.info():
                setattr(response, k, v)

        return response

