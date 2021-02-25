N=int(input())

def testcase(N):
    if N%2 !=0:
        print("weird")
    elif N%2 ==0:
        if 2 <=N <=5:
            print("Not Weird")
        elif 6 <=N <=20:
            print("weird")
        elif N > 20:
            print("Not weird")
    return;
import geojson
from descartes import PolygonPatch
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
 
with open(r"C:\Users\ankuspat\kpi\app\KPI PROJECT\WIRELESS ONE DATA\indian_village_boundaries-master\mh1.geojson") as json_file:
    json_data = geojson.load(json_file)
    
    
plt.clf()
ax = plt.figure(figsize=(10,10)).add_subplot(111)#fig.gca()
 
m = Basemap(projection='robin', lon_0=0,resolution='c')
m.drawmapboundary(fill_color='white', zorder=-1)
m.drawparallels(np.arange(-90.,91.,30.), labels=[1,0,0,1], dashes=[1,1], linewidth=0.25, color='0.5',fontsize=14)
m.drawmeridians(np.arange(0., 360., 60.), labels=[1,0,0,1], dashes=[1,1], linewidth=0.25, color='0.5',fontsize=14)
m.drawcoastlines(color='0.6', linewidth=1)
testcase(N)
