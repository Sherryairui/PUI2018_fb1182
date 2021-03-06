from __future__ import print_function
import sys
import json
try:
   import urllib2 as urllib
except ImportError:
   import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Usage: python get_bus_info_fb1182.py <MTA Key> <Bus Line> mycvs.csv")
    sys.exit()


bus_line = sys.argv[2]
key = sys.argv[1]
filename = sys.argv[3]
bus_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(key, bus_line)

response = urllib.urlopen(bus_url)
data = response.read().decode("utf-8")
data = json.loads(data)


detail = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
with open(filename, 'w') as f:	
	for i in range(len(detail[0]['VehicleActivity'])):
		line = "{},{},{},{}\n".format(detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'], detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'], detail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'])	
		f.write(line)
