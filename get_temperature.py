#!/usr/bin/python3

import json
import urllib.request
import argparse

# Source data, term and conditions https://www.geo.admin.ch/en/about-swiss-geoportal/responsabilities-and-contacts.html
url = "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-lufttemperatur-10min/ch.meteoschweiz.messwerte-lufttemperatur-10min_fr.json"


# Get temperature at specified station
def get_temperature(station_name):
    contents = urllib.request.urlopen(url).read()
    data = json.loads(contents.decode('utf-8'))

    for feature in data['features']:
        if feature['properties']['station_name'] == station_name:
            return feature['properties']['value']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get temperature at specified station')
    parser.add_argument('station_name', nargs=1, help='station (city) to search')

    args = parser.parse_args()

    print(get_temperature(args.station_name[0]))
