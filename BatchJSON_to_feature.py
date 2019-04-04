import arcpy
from arcpy import env
import os
import glob

dirOfJSON               = 'C:\\USSolar\\Data\\State\\CO\\ParcelScrape' #path to folder where .json files are stored
outputDirectory         = 'C:\\USSolar\\Data\\State\\CO\\Montrose_shp' #path to where the shapefiles will be stored

out_parcels             = "Parcel/Montrose" #name of county after forward slash
phi                     = "_DeleteTemp"


arcpy.env.workspace = dirOfJSON

for f in arcpy.ListFiles('*.json'):
    j = os.path.join(dirOfJSON, f)
    outputShp = os.path.join(outputDirectory, os.path.splitext(f)[0] + '.shp')
    print outputShp
    print("Processing : {}".format(outputShp))
    arcpy.JSONToFeatures_conversion(j, outputShp)

env.workspace           = "C:\USS\United States Solar Corporation\Site Selection - Documents\Data\State\CO\Colorado20190401.gdb" #path to .gdb
env.overwriteOutput     = True

shp = glob.glob("{}\*.shp".format(outputDirectory))
#fcs = arcpy.ListFeatureClasses()
arcpy.Merge_management(shp, out_parcels)
