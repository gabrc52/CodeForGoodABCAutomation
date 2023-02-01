# Imports aren't needed in the console,
# but they are here so VSCode/IDEs can be happy and autocomplete :)
from qgis.core import *
import processing
import os

# PASTE THE CODE BELOW INTO QGIS CONSOLE

# Change this to the path where you're storing this folder
os.chdir("/home/rgabriel/MIT/soph/IAP/6.S187/automation")


def get_tract_filename(year):
    """
    Gets the relative path of the shp file of the census tract lines
    for the specified year (None if it does not exist)
    """
    dirname = f"tract_{year}"
    if dirname not in os.listdir("downloaded/tract"):
        return None
    dir = f"downloaded/tract/{dirname}"
    tract_shp_files = [
        file
        for file in os.listdir(dir)
        if file.endswith(".shp") and "tract" in file and "tractcounty" not in file
    ]
    assert len(tract_shp_files) == 1
    return f"{dir}/{tract_shp_files[0]}"


def get_relevant_census_tracts(year):
    """
    Get a list of the relevant IDs of the tracts that overlap with the
    boundary of the area of study, for the given year
    """
    filename = get_tract_filename(year)
    result = processing.run(
        "native:joinattributesbylocation",
        {
            "INPUT": filename,
            "PREDICATE": [0],
            "JOIN": "boundary.shp",
            "JOIN_FIELDS": [],
            "METHOD": 0,
            "DISCARD_NONMATCHING": True,
            "PREFIX": "",
            "OUTPUT": "TEMPORARY_OUTPUT",
        },
    )
    layer = result['OUTPUT']
    try:
        return [feature["GEOID"] for feature in layer.getFeatures()]
    except KeyError:
        # TODO: handle
        return 'Different format!'


if __name__ == "__console__":
    tract_dict = {}
    for year in range(1960, 2022):
        filename = get_tract_filename(year)
        if filename is not None:
            tract_dict[year] = get_relevant_census_tracts(year)
