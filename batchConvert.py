# Add geopackages reading to it better formatted so that tables can be added. Will need a specific part of the loop.
# Add driver as a choosable input - done
# Add option to select which files or which depends which files are in the folder so it doesn't discriminate.
# Make it so it can change 'any OGR file to any other OGR file'.

import geopandas as gpd
import os
import sys

# These are for folder dialogue prompt
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pywin.dialogs.list


def batchConvert():
    # Select input directory
    inputPath = askdirectory(title="Select Input Directory")
    print(inputPath)
    if not inputPath:
        print("No input path detected, ending program")
        sys.exit()

    # Select output directory
    outputPath = askdirectory(title="Output directory for converted files")
    if not outputPath:
        print("No output path selected, ending program")
        sys.exit()
    # Dialogue box to select the driver part of gpd.to_file
    # Dialogue from this answer: https://stackoverflow.com/questions/68469243/dialog-box-to-select-option-from-list-in-python-on-windows
    # For some reason pywin.dialogs.list returns index of the list. Used the index to select from the options List.
    driverOptions = ["GeoJSON", "GPKG", "ESRI Shapefile", "GML"]
    conversionDriverList = pywin.dialogs.list.SelectFromList(
        "Select Driver", driverOptions
    )
    conversionDriver = driverOptions[conversionDriverList]

    # Select files by just .shp
    # https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    # shape file conversion: https://stackoverflow.com/questions/43119040/shapefile-into-geojson-conversion-python-3
    for file in os.listdir(inputPath):
        if file.endswith(".shp"):
            fullPath = os.path.join(inputPath, file)

            # reads it and stores it temporarily as a geodataframe.
            gdf = gpd.read_file(fullPath)

            # file name and path creation
            outputFileName = os.path.splitext(file)[0] + "." + str(conversionDriver)
            outputFullPath = os.path.join(outputPath, outputFileName)

            gdf.to_file(outputFullPath, driver=str(conversionDriver))

            print(f"Converted {file} to GeoJSON and saved as {outputFileName}")


batchConvert()


# Supported drivers
""" {
    "AeronavFAA": "r",
    "ARCGEN": "r",
    "BNA": "raw",
    "DXF": "raw",
    "CSV": "raw",
    "OpenFileGDB": "r",
    "ESRIJSON": "r",
    "ESRI Shapefile": "raw",
    "GeoJSON": "rw",
    "GPKG": "rw",
    "GML": "raw",
    "GPX": "raw",
    "GPSTrackMaker": "raw",
    "Idrisi": "r",
    "MapInfo File": "raw",
    "DGN": "raw",
    "S57": "r",
    "SEGY": "r",
    "SUA": "r",
    "TopoJSON": "r",
} """
# from fiona
{
    "DXF": "rw",
    "CSV": "raw",
    "OpenFileGDB": "raw",
    "ESRIJSON": "r",
    "ESRI Shapefile": "raw",
    "FlatGeobuf": "raw",
    "GeoJSON": "raw",
    "GeoJSONSeq": "raw",
    "GPKG": "raw",
    "GML": "rw",
    "OGR_GMT": "rw",
    "GPX": "rw",
    "Idrisi": "r",
    "MapInfo File": "raw",
    "DGN": "raw",
    "PCIDSK": "raw",
    "OGR_PDS": "r",
    "S57": "r",
    "SQLite": "raw",
    "TopoJSON": "r",
}
