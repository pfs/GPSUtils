#!/usr/bin/env python

import sys
from time import gmtime, strftime

def createWaypointRoute(name,wptList,outF):

    """creates a waypoint route from a list of (latitude,longitude,name)"""

    f=open(outF,'w')

    #header
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    f.write('<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd">\n')

    #metadata
    f.write('<metadata>\n')
    tstr=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    f.write('<link href="http://www.garmin.com"><text>Garmin International</text></link>\n')
    f.write('<time>%s</time>\n'%tstr)
    f.write('</metadata>\n')

    #the route
    f.write('<rte>\n')
    f.write('<name>{0}</name>\n'.format(name))
    for lat,lon,_,name in wptList:
        f.write('<rtept lat="{0}" lon="{1}"><name>{2}</name></rtept>\n'.format(lat,lon,name))
    f.write('</rte>\n')
    f.write('</gpx>\n')
    f.close()

def parseWaypointListFrom(inF):

    """reads a list of waypoints from a txt file"""

    wptList=[]

    f=open(inF,'r')
    lines=f.read().splitlines()
    for l in lines:
        lat,lon,height=l.split()
        lat = lat.translate(None, 'NSEW')
        lon = lon.translate(None, 'NSEW')
        name='pt%d'%(len(wptList)+1)
        wptList.append( (lat,lon,height,name) )
    f.close()

    return wptList


def main():

    inF,name,outF=sys.argv[1:4]
    outF += '.gpx'

    print 'Parsing waypoints from',inF
    wptList=parseWaypointListFrom(inF=inF)

    print 'Creating route in gpx format',outF
    createWaypointRoute(name=name,wptList=wptList,outF=outF)


if __name__ == "__main__":
    main()

