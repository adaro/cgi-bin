###
#Very basic Mock Test
#It allows you to replace parts of
#your system with mock objects
#and make assertions about how
#they have been used.
###

import urllib2
from StringIO import StringIO

def mock_response(req):
    if req.get_full_url() == "http://wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d":
        resp = urllib2.addinfourl(StringIO("mock response:"), "mock message", req.get_full_url())
        resp.code = 200
        resp.msg = "OK"
        return resp

class MockHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return mock_response(req)

if __name__ == "__main__":
    #urllib2 has functions called build_opener()
    #and install_opener() which we can use to mock
    #the behaviour of urlopen()
    my_opener = urllib2.build_opener(MockHTTPHandler)
    urllib2.install_opener(my_opener)
    url = "http://wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d"
    response=urllib2.urlopen(url)
    print response.read()
    print response.code
    print response.msg
