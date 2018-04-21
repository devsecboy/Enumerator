asimport os, errno

class GlobalVariables(object):
    def __init__(self):
    	self.hackerOneURL = 'https://hackerone.com/'
    	self.bugCrowdURL = 'https://www.bugcrowd.com/'
    	self.hackerOneProgramsURL = 'https://hackerone.com/bug-bounty-programs'
    	self.bugCrowdProgramsURL = 'https://www.bugcrowd.com/bug-bounty-list/'
    	self.testSSLPath = "./testssl.sh"
    	self.programURLs = "ProgramsURL.txt"
    	self.httpUAHeader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}