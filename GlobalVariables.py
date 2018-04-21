import re

class GlobalVariables(object):
    def __init__(self):
    	self.hackerOneURL = 'https://hackerone.com/'
    	self.bugCrowdURL = 'https://www.bugcrowd.com'
    	self.hackerOneProgramsURL = 'https://hackerone.com/programs/search?query=bounties%3Ayes&sort=name%3Aascending&page='
    	self.bugCrowdProgramsURL = 'https://bugcrowd.com/programs?page='
    	self.testSSLPath = "./testssl.sh"
    	self.programURLs = "ProgramsURL.txt"
    	self.pattern = "((https?:\/\/)?(?:www\.|(?!www))[a-zA-Z0-9*][a-zA-Z0-9-*]+[a-zA-Z0-9*]\.[^\s]{2,}|www\.[a-zA-Z0-9*][a-zA-Z0-9-*]+[a-zA-Z0-9*]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9*]\.[^\s]{2,}|www\.[a-zA-Z0-9*]\.[^\s]{2,})"
    	self.findHostName = re.compile(self.pattern)
    	self.totalBugCrowdPage=4
    	self.totalHackeronePage=3
    	self.httpUAHeaderBugCrowd={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    	self.httpUAHeader = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
							'Accept': 'application/json, text/javascript, */*; q=0.01',
							'X-Requested-With': 'XMLHttpRequest'}