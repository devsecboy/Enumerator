import sys
import requests
from bs4 import BeautifulSoup
import os
import subprocess
import urllib2
from GlobalVariables import *

class BugCrowd:
    def __init__(self):
        self.globalVariables=GlobalVariables()

    def EnumerateBugCrowd(self, domain, nodomain, wildcardDomain):
        try:
            i=1
            while i <= self.globalVariables.totalBugCrowdPage:
                request = requests.get(self.globalVariables.bugCrowdProgramsURL+str(i), headers=self.globalVariables.httpUAHeaderBugCrowd, timeout=10)
                soup = BeautifulSoup(request.text, "lxml")
                for program in soup.findAll("h4", { "class" : "bc-panel__title" }):
                    hrefTag = program.find('a', href=True)
                    programURL= hrefTag.get('href')
                    try:
                        if programURL.find("https://www.bugcrowd.com/resource/help-wanted") < 0:
                            programURL = self.globalVariables.bugCrowdURL+programURL
                            request = requests.get(programURL, headers=self.globalVariables.httpUAHeaderBugCrowd, timeout=10)
                            subSoup = BeautifulSoup(request.text, "lxml")
                            scopeURLs=subSoup.findAll("li", { "class" : "bc-target" })
                            for scopeURL in scopeURLs:
                                hostname=scopeURL.find('code').text
                                hostname=hostname[0:hostname.find("\n")]
                                print hostname
                                if hostname[0] == '*':
                                    wildcardDomain.append(hostname);
                                else:
                                    if self.globalVariables.findHostName.match(hostname) is not None:
                                        domain.append(hostname)
                                    else:
                                        nodomain.append(hostname)
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