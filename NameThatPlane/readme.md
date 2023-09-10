# Name That Plane Writeup

## Challenge

You are given `Plane.png` and `airport.png`.  The challenge is to find the name of the plane and the airport.

## Solution


1. Overlay the airport image with a protractor to determine the heading of the runway (runways are labeled by the first two digits of their heading).  The runway appears to be around 7 degrees, which means it's likely runway 01/19.  Additionally, it appears to be about 200ft wide, because the distance between the middle of each white centerline is 200ft.  It also appears that this is the only runway at this airport based on the picture.

2. Find the included `runways.csv` file which lists every runway in the world.  (https://github.com/chandanverma07/DataSets/blob/master/runways.csv)

3. Using all of this, filter the `runways.csv` file with a python script, and open a link to Google Maps with each coordinate.  Then, ctrl+tab through all the tabs until the right one appears.

4. Zoom into the upper left area of the runway to find the plane, see that it is near helicopters and assume it is a military aicraft, and use Wikipedia to list the Afganistan Air Force aircraft inventory.  Only one plane matches the size and shape of the plane shown in the picture.
