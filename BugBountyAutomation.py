from BugCrowd import *
from HackerOne import *

if __name__ == "__main__":
	domains=list()
	nodomains=list()
	wildcardDomains=list()

	hackerone=HackerOne()
	hackerone.EnumerateHackerOne(domains, nodomains, wildcardDomains)
	bugCrowd = BugCrowd()
	bugCrowd.EnumerateBugCrowd(domains, nodomains, wildcardDomains)

	domainFile = open("domain.txt","w")
	noDomainFile = open("nodomain.txt","w")
	wildDomainFile = open("wilddomain.txt","w")
	for domain in domains:
		domainFile.write(domain + "\n")
	for domain in nodomains:
		noDomainFile.write(domain + "\n")
	for domain in wildcardDomains:
		wildDomainFile.write(domain + "\n")