####
#This file is a "wrapper" for the NprFeed class.
#also acts as our "template" for (in this case) printing our HTML.
#This wrapper helps us separate presentation layer from our business logic
#For the sake of simplicity we will just print the HTML.
####

#python libs
import cgitb
import pprint

#custom module
from server import NprFeed

class Wrapper(object):
    def __init__(self):
        #instantiate class
        self.wd_instance = NprFeed()

    def render_html(self):
        #run instance method
        entry_list = self.wd_instance.return_list()
        entries = list(self.wd_instance.return_list())
        #print HTML. Keeping it simple =) 
        print("Content-type: text/html")
        print
        print("<title>NprFeed Test</title>")
        print("<h1> Smallest Thumbnail </h1>")
        print("<hr>")
        #loop over entry_list, and get the min value for 'fileSize'
        #using a fancy pancy list comprehension =)
        seq = [x['fileSize'] for x in entry_list]
        smallest_thumbnail = min(seq)
        while entry_list:
            dicti = entry_list.pop()
            if dicti['fileSize'] == smallest_thumbnail:
                formatted_dict = pprint.pformat(dicti)
                print("<pre>" +  formatted_dict + "</pre>")
                print("<img src=" + dicti["url"] + ">")

        #loop over entry list again and this time pprint all dicts.	
        print "<h1> All Dictionary Values </h1>"
        print "<hr>"
        while entries:
            dicti = entries.pop()
            formatted_dict = pprint.pformat(dicti)
            print("<pre>" +  formatted_dict + "</pre>")

if __name__ == "__main__":
    #enable cgitb
    cgitb.enable()    
    run = Wrapper()
    run.render_html()
