from math import *
from random import *
import urllib2, json
import re
import os  
import time
import urllib
import nude
from nude import Nude
from PIL import Image

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
compteur=0
while True:
    tag = str(choice(tableau)) + str(choice(tableau)) + str(choice(tableau)) + str(choice(tableau))
    mdr = str(choice(tableau)) + str(choice(tableau)) + str(choice(tableau)) + str(choice(tableau))

    input = "http://screencloud.net/v/"+tag
    print bcolors.HEADER + input + " Essai numero "+str(compteur) + bcolors.ENDC
    try:
        response = urllib2.urlopen(input)

        html = response.read()
     
        m = re.search("<img.+?src=[\"'](.+?)[\"'].*?>",html)
        if m is not None:
           lol= m.group(0)
    

        m = re.search("/(.+?)png",lol)
        if m is not None:
          lol2= m.group(0)
       

        input = "https:"+lol2 
        
        urllib.urlretrieve(input, "/Users/julienmalka/Desktop/UplmgNudeLocator/images/"+mdr+".png")
        n = Nude('/Users/julienmalka/Desktop/UplmgNudeLocator/images/'+mdr+".png")
        n.parse()
        
        
        if n.result==False:
          print bcolors.OKGREEN + "No nude on this one" + bcolors.ENDC
          os.remove("/Users/julienmalka/Desktop/UplmgNudeLocator/images/"+mdr+".png")


          
        else:
          print bcolors.OKBLUE + "Nude Found" + bcolors.ENDC
          
  

    except urllib2.HTTPError, e:
       print bcolors.FAIL + "URL est une 404" + bcolors.ENDC
    
    compteur= compteur +1
 