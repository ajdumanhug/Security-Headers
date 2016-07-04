import sys
import urllib2

url = raw_input('Enter the url: ')

if url.startswith("http://"):
    url = url
elif url.startswith("https://"):
    url = url
elif not url.startswith("http://") or not url.startswith("https://"):
        url = "http://"+ url
else:
    print ("Sorry! We can't recognize your input.")
    sys.exit()

request = urllib2.Request(url)
response = urllib2.urlopen(request)
securityHeaders = response.headers

print ("\nSecurity Headers:\n")

if "Strict-Transport-Security" in securityHeaders:
    print (" > Strict-Transport-Security")

if "X-Frame-Options" in securityHeaders:
    print (" > X-Frame-Options")

if "X-XSS-Protection" in securityHeaders:
    print (" > X-XSS-Protection")

if "X-Content-Type-Options" in securityHeaders:
    print (" > X-Content-Type-Options")

if "Content-Security-Policy" in securityHeaders:
    print (" > Content-Security-Policy")

if "Cache-Control" in securityHeaders:
    print (" > Cache-Control")

if "X-Download-Options" in securityHeaders:
    print (" > X-Download-Options")

if "X-Permitted-Cross-Domain-Policies" in securityHeaders:
    print (" > X-Permitted-Cross-Domain-Policies")

if "Public-Key-Pins" in securityHeaders:
    print (" > Public-Key-Pins")

if "Public-Key-Pins-Report-Only" in securityHeaders:
    print (" > Public-Key-Pins-Report-Only")

print ("\nMissing Headers:\n")

if "Strict-Transport-Security" not in securityHeaders:
    print (" > Strict-Transport-Security")

if "X-Frame-Options" not in securityHeaders:
    print (" > X-Frame-Options")

if "X-XSS-Protection" not in securityHeaders:
    print (" > X-XSS-Protection")

if "X-Content-Type-Options" not in securityHeaders:
    print (" > X-Content-Type-Options")

if "Content-Security-Policy" not in securityHeaders:
    print (" > Content-Security-Policy")

if "Cache-Control" not in securityHeaders:
    print (" > Cache-Control")

if "X-Download-Options" not in securityHeaders:
    print (" > X-Download-Options")

if "X-Permitted-Cross-Domain-Policies" not in securityHeaders:
    print (" > X-Permitted-Cross-Domain-Policies")

if "Public-Key-Pins" not in securityHeaders:
    print (" > Public-Key-Pins")

if "Public-Key-Pins-Report-Only" not in securityHeaders:
    print (" > Public-Key-Pins-Report-Only")

response.close()