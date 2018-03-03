import sys
import urllib2
import re
import argparse

parser = argparse.ArgumentParser(description = "It is a python tool developed to enumerate security headers of a website.")
parser.add_argument("--url", "-u", action = "store", dest = "url", required = False, help = "Enter the url")
arguments = parser.parse_args()


if arguments.url:
	url = arguments.url
else:
	url = raw_input("Enter the url: ")

if url.startswith("http://"):
    url
elif url.startswith("https://"):
    url
elif not url.startswith("http://") or not url.startswith("https://"):
    url = "http://"+ url
else:
    print ("Sorry! We can't recognize your input.")
    sys.exit()

request = urllib2.Request(url)
response = urllib2.urlopen(request)
securityHeaders = response.headers

headers = ["Strict-Transport-Security","X-Frame-Options","X-XSS-Protection","X-Content-Type-Options","Content-Security-Policy",
        "Cache-Control","X-Download-Options","X-Permitted-Cross-Domain-Policies","Public-Key-Pins","Public-Key-Pins-Report-Only"]

print ("\nSecurity Headers Found:\n")

for header in headers:
    if header in securityHeaders:
	if (header == "Strict-Transport-Security"):
		max_age = re.findall("max-age=(\w*)", securityHeaders["strict-transport-security"])[0]
		if (int(max_age) < 10368000):
			print ("\033[91m > " + header + ": " + securityHeaders[header] + "\033[0m\n    + Max-age is lower than 10368000 (seconds)\n    (https://blog.qualys.com/securitylabs/2016/03/28/the-importance-of-a-proper-http-strict-transport-security-implementation-on-your-web-server)\n")
        else:
		    print (" > " + header)


print ("\nMissing Headers:\n")

for header in headers:
    if header not in securityHeaders:
        print (" > " + header)

response.close()
