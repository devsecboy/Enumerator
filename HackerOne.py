import sys
import requests
from bs4 import BeautifulSoup
import os
import urllib2
import json
from AttackMethods import *

class HackerOne:
    def __init__(self):
    	self.attackMethods = AttackMethods()
        self.hackerOneURL = 'https://hackerone.com/programs/search?query=bounties%3Ayes&sort=name%3Aascending&limit=1000'
        self.url = 'https://hackerone.com'
        self.directory = 'none'
        self.testSSLPath = os.getcwd() + "/testssl"

        #specific header is required to get the json response from hackerOne
        self.httpUAHeader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'X-Requested-With': 'XMLHttpRequest'}

    def EnumerateHackerOne(self):

        #Create new file
        command = "echo StartExecution > ./AllURLS.txt"
        print os.popen(command).read()

        request = requests.get(self.hackerOneURL) 
        data = json.loads(request.text)
        for program in data['results']:
            programURL = self.url + program['url']
            programName = program['name']

            command = "echo \"\n" + programName + "\t"+ programURL +"\" >> ./AllURLS.txt"
            print os.popen(command).read()
            
            newRequest = requests.get(programURL, headers=self.httpUAHeader)
            scopes = json.loads(newRequest.text)
            for scope in scopes['scopes']:
                hostname = scope.replace("*.", "")
                command = "echo " + hostname + " >> ./AllURLS.txt"
                print os.popen(command).read()
                #self.attackMethods.CheckHTTP10Vulnearability(hostname, programName)
                #self.attackMethods.CheckTestSSLVulnerability(hostname, programName)
                #self.attackMethods.CheckDirbVulnerability(hostname, programName)
                #self.attackMethods.CheckTemplateInjectionVulnerability(hostname, programName)
                #self.attackMethods.CheckOPTIONSMethodVulnerability(hostname, programName)
                #self.attackMethods.CheckforSubdomainTakeover(url, programName)
                self.attackMethods.CheckForEmailSpoofing(hostname)