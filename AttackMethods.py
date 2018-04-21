import subprocess

try:
    from httplib import HTTPConnection
    from urllib2 import HTTPHandler, build_opener
except ImportError: # Python 3
    from http.client import HTTPConnection
    from urllib.request import HTTPHandler, build_opener

class HTTP10Connection(HTTPConnection):
    _http_vsn = 10
    _http_vsn_str = "HTTP/1.0" 

class AttackMethods:
	def __init__(self):
		#Initialize any variable if required
		test = 'a'

	def CheckHTTP10Vulnearability(self, url, programName):
		try:
			print url
			opener = build_opener(HTTP10Handler)
			print(opener.open(url).read()[:100])
		except:
			print url

	def CheckTestSSLVulnerability(self, url, programName):
		command = "./testssl.sh/testssl.sh " + url + " > ./" + programName + "/TestSSLResult.txt"
		print os.popen(command).read()

	def CheckDirbVulnerability(self, url, programName):
		command = "./dirb/dirb " + url + " > ./" + programName + "/DirBusterResult.txt"
		print os.popen(command).read()

	#it is reuired paramerized request, currently it is not possible to test
	def CheckTemplateInjectionVulnerability(self, url, programName):
		command = "python ./tplmap/tplmap.py " + url + " > ./" + programName + "/TPLMAPResult.txt"
		print os.popen(command).read()

	def CheckOPTIONSMethodVulnerability(self, url, programName):
		try:
			opener = urllib2.build_opener(urllib2.HTTPHandler)
			request = urllib2.Request(url)
			request.get_method = lambda: 'OPTIONS'
			url = opener.open(request)
		except:
			print url

	def CheckforSubdomainTakeover(self, url, programName):
		command = "knockpy " + url + " > ./" + programName + "/Knockpy.txt"
		print command
		print os.popen(command).read()

	def CheckForEmailSpoofing(self, domainName)
		command = "dig TXT " + domainName
		print command
		print os.popen(command).read()

	def CheckForKnownFiles(self, domainName):
		#server-status
