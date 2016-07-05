import sys
import urllib2

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

print ("\nSecurity Headers:\n")

for header in headers:
    if header in securityHeaders:
        print (" > " + header)


print ("\nMissing Headers:\n")

for header in headers:
    if header not in securityHeaders:
        print (" > " + header)

response.close()
