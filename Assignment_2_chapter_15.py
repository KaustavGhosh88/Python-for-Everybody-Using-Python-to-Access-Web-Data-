import urllib
import json

service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

address = raw_input ("Enter location: ")
url = service_url+urllib.urlencode({'address': address})

print "Retieving",url
url_h = urllib.urlopen(url)
data = url_h.read()
    
info = json.loads(str(data))
print json.dumps(info, indent=4)

print "Place id", info["results"][0]["place_id"]