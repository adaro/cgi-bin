####
#This file is a "wrapper" for the WireDriveTest class.
#also acts as our "template" for (in this case) printing our HTML.
#This wrapper helps us separate presentation layer from our business logic
#This is NOT how I would normally go about rendering HTML.
#I wanted to keep this code light and not juggle a bunch of
#dependencies. For the sake of simplicity we will just print the HTML.
####

#python libs
import cgitb
import pprint

#custom module
from server import WireDriveTest

class Wrapper(object):
    def __init__(self):
        #instantiate class
        self.wd_instance = WireDriveTest()

    def render_html(self):
        #run instance method
        entry_list = self.wd_instance.return_list()
        #Running return_list() twice just to display the
        #while style of looping below. The while pops items
        #from list so you are left with an empty list at the end.
        #We could easily use a for loop if we wanted.
        entries = list(self.wd_instance.return_list())
        #print HTML. Keeping it simple =) 
        print("Content-type: text/html")
        print
        print("<title>WireDrive Test</title>")
        print("<h1> Smallest Thumbnail </h1>")
        print("<hr>")
        #loop over entry_list, and get the min value for 'fileSize'
        #using a fancy pancy list comprehension =)
        seq = [x['fileSize'] for x in entry_list]
        smallest_thumbnail = min(seq)

        #loop to get the smallest thumbnail. There is probably a more 
        #pythonic way of doing this, but hey.. it works. Finally, pretty format
        #the dictionary and display the thumbnail using the img HTML tag.
        while entry_list:
            #pop items out of list to keep memory footprint low
            #if this was a giant list, we would see some big speed 
            #improvements
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
