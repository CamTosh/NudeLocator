from math import *
from random import *
import urllib2, json
import re
from os.path import abspath,expanduser
import os  
import time

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


tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
compteur=0
while True:
    tag = str(choice(tableau)) + str(choice(tableau)) + str(choice(tableau))


    input = "http://uplmg.com/"+tag
    print bcolors.HEADER + input + " Essai numero "+str(compteur) + bcolors.ENDC
    try:
        response = urllib2.urlopen(input)

        html = response.read()
        m = re.search("<img.+?src=[\"'](.+?)[\"'].*?>",html)
        if m is not None:
           lol= m.group(0)


        m = re.search("/(.+?)g",lol)
        if m is not None:
          lol2= m.group(0)


        input = "http://uplmg.com"+lol2 
        request = urllib2.Request('https://api.algorithmia.com/v1/algo/sfw/NudityDetection/0.1.69')
        request.add_header('Content-Type', 'application/json')
        request.add_header('Authorization', 'Simple simpC5LBCivxfwEwCiIIQlSAy3m1')
        response = urllib2.urlopen(request, json.dumps(input))
        lol10 =response.read()

        if "Not" in lol10:
          print bcolors.OKGREEN + "No nude on this one" + bcolors.ENDC
          
          
        else:
          print bcolors.OKBLUE + "Nude Found" + bcolors.ENDC
          fh = open('/Users/julienmalka/Desktop/lol.txt', 'a')
          fh.write(input+"\n")
          fh.close()
  

    except urllib2.HTTPError, e:
       print bcolors.FAIL + "URL est une 404" + bcolors.ENDC
    
    compteur= compteur +1
    time.sleep(1)
   
   