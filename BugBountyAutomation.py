from BugCrowd import *
from HackerOne import *

if __name__ == "__main__":
	domainFile = open("domain.txt","w")
	noDomainFile = open("nodomain.txt","w")
	wildDomainFile = open("wilddomain.txt","w")

	domain=list()
	nodomain=list()
	wildcardDomain=list()
	hackerone=HackerOne()
	hackerone.EnumerateHackerOne(domain, nodomain, wildcardDomain)
	domainFile.write(domain)
	noDomainFile.write(nodomain)
	wildDomainFile.write(wildcardDomain)

	domain=list()
	nodomain=list()
	wildcardDomain=list()
	bugCrowd = BugCrowd()
	bugCrowd.EnumerateBugCrowd(domain, nodomain, wildcardDomain)
	domainFile.write(domain)
	noDomainFile.write(nodomain)
	wildDomainFile.write(wildcardDomain)