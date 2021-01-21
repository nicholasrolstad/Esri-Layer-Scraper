import arcpy
import os
import glob

name = 'Peoria'
# general parameters
input_directory = r'C:\Users\NicholasRolstad\Desktop\{}'.format(name) # path to folder where .json files are stored
output_directory = r'C:\Users\NicholasRolstad\Desktop\{}'.format(name) # path to where the converted shapefiles will be stored.
gdb = False # True = Feature Class output, False = Shapefile output

# Feature Class Output Parameters
gdb_path = r'C:\Users\NicholasRolstad\Desktop\GDB\COParcel.gdb' #path to .gdb
feature_dataset = '' #name of feature dataset (i.e. Parcel)
feature_class = '' # name of feature dataset output (probably the county name or something like 'ParcelsHennepin')
phi = "_DeleteTemp"

# Shapefile Output Parameters
shp_output_path = r'C:\Users\NicholasRolstad\Desktop\{}'.format(name) # path to the merged shapefile output
shapefile_name = 'Parcels{}'.format(name) # (probably the county name or something like 'ParcelsHennepin')

if gdb:
    arcpy.env.workspace = input_directory
    
    for f in arcpy.ListFiles('*.json'):
        j = os.path.join(input_directory, f)
        output_shp = os.path.join(output_directory, os.path.splitext(f)[0] + '.shp')
        print("Processing : {}".format(output_shp))
        arcpy.JSONToFeatures_conversion(j, output_shp)
    
    arcpy.env.workspace = gdb_path
    shp = glob.glob("{}\*.shp".format(output_directory))
    output = '{}/{}'.format(feature_dataset, feature_class)
    arcpy.Merge_management(shp, output)
else:
    arcpy.env.workspace = input_directory
    
    for f in arcpy.ListFiles('*.json'):
        j = os.path.join(input_directory, f)
        outputShp = os.path.join(output_directory, os.path.splitext(f)[0] + '.shp')
        print("Processing : {}".format(outputShp))
        arcpy.JSONToFeatures_conversion(j, outputShp)
    
    
    arcpy.env.workspace = shp_output_path
    shp = glob.glob("{}\*.shp".format(output_directory))
    output = '{}/{}'.format(shp_output_path, shapefile_name)
    arcpy.Merge_management(shp, output)
