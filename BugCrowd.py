import sys
import requests
from bs4 import BeautifulSoup
import re
import os
import subprocess
import urllib2
from AttackMethods import *

class BugCrowd:
    def __init__(self):
    	self.attackMethods = AttackMethods()
    	self.bugCrowdBaseURL = 'https://bugcrowd.com'
    	self.url = 'https://bugcrowd.com/programs'
    	self.directory = 'none'
    	self.httpUAHeader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    	self.validHostName = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})"
    	self.pattern = re.compile(self.validHostName)
        self.testSSLPath = os.getcwd() + "/testssl"

    def EnumerateBugCrowd(self):

        #Create new file
        command = "echo StartExecution > ./AllURLS.txt"
        print os.popen(command).read()

        request = requests.get(self.url, headers=self.httpUAHeader)
        soup = BeautifulSoup(request.text, "lxml")
        for program in soup.findAll("div", { "class" : "bounty-header" }):
        	hrefTag = program.find('a', href=True)
        	self.IdentifyProgramScope(hrefTag['href'], hrefTag.text)

        i = 2
        while i < 4:
        	nextURL = self.url + '?page=' + str(i)
        	request = requests.get(nextURL, headers=self.httpUAHeader)
        	soup = BeautifulSoup(request.text, "lxml")
        	for program in soup.findAll("div", { "class" : "bounty-header" }):
        		hrefTag = program.find('a', href=True)
        		self.IdentifyProgramScope(hrefTag['href'], hrefTag.text)
        	i += 1

    def IdentifyProgramScope(self, programLink, programName):
        try:
            command = "echo \"\n" + programName + "\t"+ self.bugCrowdBaseURL +programLink +"\" >> ./AllURLS.txt"
            print os.popen(command).read()

            programName = "./Output/" + programName.strip()
            if not os.path.exists(programName):
                os.makedirs(programName)
            programURL = self.bugCrowdBaseURL + programLink
            print programURL
            request = requests.get(programURL, headers=self.httpUAHeader)
            soup = BeautifulSoup(request.text, "lxml")
            scopeUL = soup.find("ul", { "class" : "targets" })
            for program in scopeUL.findAll("li"):
                hostname = program.text.replace("*.", "www.")
                urls = re.findall(self.validHostName, hostname)
                for url in urls:
                    command = "echo \t" + url + " >> ./AllURLS.txt"
                    print os.popen(command).read()
                    #self.attackMethods.CheckHTTP10Vulnearability(url, programName)
                    #self.attackMethods.CheckTestSSLVulnerability(url, programName)
                    #self.attackMethods.CheckDirbVulnerability(url, programName)
                    #self.attackMethods.CheckTemplateInjectionVulnerability(url, programName)
                    #self.attackMethods.CheckOPTIONSMethodVulnerability(url, programName)
                    #self.attackMethods.CheckforSubdomainTakeover(url, programName)
                    self.attackMethods.CheckForEmailSpoofing(hostname)

        except:
            print programLink