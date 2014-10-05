#No shebang line. File is meant to be imported

####
#This file acts as our server class used to parse the RSS feed
#and calculate bit_rate and video_compression. This class is also
#responsible for building the final dictionary of items
####

#python libs
import urllib2
from xml.etree import ElementTree as etree

class NprFeed(object):
    """
    Server class used to parse
    RSS feed and build dictionary
    """
    def __init__(self):
        #initialization method used to create instance vars
        self.items = self.fetch_item()
        self.entry_list = self.loop_items(self.items)

    def return_list(self):
        #method simply returns instace var 
        return self.entry_list
        
    #methods for calculating video bit rate/compression, useful for predetermineing mememory needs
    def __calculate_bit_rate(self, dict_item):
        bit_rate = int(dict_item["fileSize"]) / int(dict_item["duration"])
        return bit_rate

    def __calculate_video_compression(self, dict_item):
        uncompressed = int(dict_item["width"]) * int(dict_item["height"]) * int(dict_item["duration"])
        video_compression = float(uncompressed)/float(dict_item["fileSize"])
        return video_compression

    def fetch_item(self):
        #Data Layer for fetching RSS feed
        wd_xml = urllib2.urlopen('http://www.npr.org/rss/rss.php?id=1001')
        #convert to string:
        xml_data = wd_xml.read()
        #close file so that we don't hit an open file
        #handle limit if this code were to run long
        wd_xml.close()
        #entire feed
        xml_root = etree.fromstring(xml_data)
        #find all items
        items = xml_root.findall('channel/item')
        return items

    def loop_items(self, item):
        #method used to loop over items, create dict and append to list
        entries = list()
        for entry in item:
            xml_feed_dict=dict()
            for key in list(entry):
                for item in key.items():
                    if item:
                        xml_feed_dict[item[0]] = item[1]
            #bit_rates = self.__calculate_bit_rate(xml_feed_dict)
            #xml_feed_dict['bitRate'] = bit_rates
            #video_compression = self.__calculate_video_compression(xml_feed_dict)
            #xml_feed_dict['videoCompression'] = video_compression
            entries.append(xml_feed_dict) 
        return entries
