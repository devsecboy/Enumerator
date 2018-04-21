import sys
import requests
from bs4 import BeautifulSoup
import os
import urllib2
import string
import json
from GlobalVariables import *

class HackerOne:
    def __init__(self):
        self.globalVariables=GlobalVariables()

    def EnumerateHackerOne(self, domain, nodomain, wildcardDomain):
        try:
            i=1
            while i <= self.globalVariables.totalHackeronePage:
                request = requests.get(self.globalVariables.hackerOneProgramsURL+str(i), headers=self.globalVariables.httpUAHeader, timeout=10) 
                data = json.loads(request.text)
                for program in data['results']:
                    programURL = self.globalVariables.hackerOneURL + program['url']
                    programName = program['name']
                    
                    try:
                        programURL=string.replace(programURL, '//', '/')
                        programURL=string.replace(programURL, ':/', '://')
                        newRequest = requests.get(programURL, headers=self.globalVariables.httpUAHeader, timeout=10)
                        scopes = json.loads(newRequest.text)
                        if len(scopes['scopes']) > 0:
                            for hostname in scopes['scopes']:
                                print hostname
                                if len(hostname) > 0:
                                    if hostname[0] == '*':
                                        wildcardDomain.append(hostname);
                                    else:
                                        domain.append(hostname);
                        else:
                            nodomain.append(programURL);
                    except Exception as exception:
                        print exception
                    else:
                        pass
                    finally:
                        pass
                i=i+1
        except Exception as e:
            print e
        else:
            pass
        finally:
            pass