import arcpy
import os

dirOfJSON = ''  # folder containing json files
outputDirectory = '' # folder to save shapefiles

arcpy.env.workspace = dirOfJSON

for f in arcpy.ListFiles('*.json'):
    j = os.path.join(dirOfJSON, f)
    outputShp = os.path.join(outputDirectory, os.path.splitext(f)[0] + '.shp')
    print("Processing : {}".format(outputShp))
    arcpy.JSONToFeatures_conversion(j, outputShp)
