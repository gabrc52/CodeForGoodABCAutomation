#!/bin/bash

# Assumption: You are using GNOME on Linux
#
# Before running this script, go to Files and navigate to ftp://ftp2.census.gov/
#
# Since this is for documentation purposes on how we did the download, there is no compatibility for Windows
# You can instead manually copy the files or use the ones that we already downloaded

FTP=/run/user/1000/gvfs/ftp:host=ftp2.census.gov

download_year() {
	year=$1
	cp $FTP/geo/tiger/GENZ$year/shp/*25_tract*.zip downloaded
	cp $FTP/geo/tiger/GENZ$year/shp/*25_bg*.zip downloaded
}

for year in {2014..2021}; do
	echo Downloading for $year...
	download_year $year
done
