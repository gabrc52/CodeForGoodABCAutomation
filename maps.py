# Imports aren't needed in the console,
# but they are here so VSCode/IDEs can be happy and autocomplete :)
from qgis.core import *
import processing
import os

# PASTE THE CODE BELOW INTO QGIS CONSOLE

# Change this to the path where you're storing this folder
os.chdir("/home/rgabriel/MIT/soph/IAP/6.S187/automation")

def joined_layer(year):
    """
    Loads the spreadsheet and block group shapefile and joins them

    The result is a new layer which only has the relevant block groups and has the data
    """
    # TODO: use the cleaned spreadsheet and make sure the types are right...
    # ...and either remove the header row or make a new one
    # csv_layer = QgsVectorLayer(f"downloaded/social_explorer/{year}.csv", f"{year}.csv", "ogr")
    bg_shapefile = [f for f in os.listdir(f"downloaded/bg/bg_{year}") if f.endswith(".shp")][0]
    # bg_layer = QgsVectorLayer(f"downloaded/bg/bg_{year}/{bg_shapefile}", f"{year} block groups", "ogr")
    result = processing.run(
        "native:joinattributestable",
        {
            "INPUT": f"downloaded/bg/bg_{year}/{bg_shapefile}",
            "FIELD": "GEOID",
            "INPUT_2": f"social_explorer_cleaned/{year}.csv",
            "FIELD_2": "Geo_FIPS",
            "FIELDS_TO_COPY": [],
            "METHOD": 1,
            "DISCARD_NONMATCHING": True,
            "PREFIX": "",
            "OUTPUT": "TEMPORARY_OUTPUT",
        },
    )
    return result['OUTPUT']


def load_joined(year):
    layer = joined_layer(year)
    QgsProject.instance().addMapLayer(layer)


def map_attribute(year, attr):
    """
    Generates a map of a given attribute (format TBD) for a given year

    Saves a PNG file (TBD)
    """
    print(f"mapping {year}")

    layer = joined_layer(year)
    QgsProject.instance().addMapLayer(layer)

    # TODO: implement
    # figure out how to do the equivalent of: right click layer > symbology > graduated
    # NOTE: use the same "classes" when comparing across years so the map symbology is consistent

    # with open(f'img/{year}_{attr}.png', 'w') as f:
    #     f.write(NotImplemented)

    QgsProject.instance().removeMapLayer(layer)



attributes = [
    NotImplemented,
    # TODO: this should be a list of all attributes, in whatever format is best for you
]

years = range(2010, 2022)

def generate_image_files():
    """
    Generate all image files, for use in the HTML viewer
    """
    # do whatever implementation is best for you
    for attribute in attributes:
        for year in years:
            map_attribute(year, attribute)


if __name__ == "__console__":
    generate_image_files()