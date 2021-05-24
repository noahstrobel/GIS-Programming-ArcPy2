# Name: Noah Strobel

# Class: GISc-450

# Created: 3/25/2021

# Purpose: This program examines shapefiles from the Corvallis GDB and prints the name, feature type, number
# of records, and then assigns them a new name based on the feature type and number of features (<= 1000 and >= 1001)
# It then creates a folder named "Strobel_data" and moves the newly-named features to said folder


import arcpy
import os
import time
import shutil

arcpy.env.overwriteOutput = True


time_start = time.time()


def main():

    print("\nThis program examines shapefiles within the Corvallis GDB and then prints their name,")
    print("feature type, and the number of records they contain. It then assigns them a new name")
    print("based on the feature type and number of records. Finally, it creates a new folder,")
    print("'Strobel_data,' and moves the newly-named features to it.")

    print("\n---Script starting---")

    arcpy.env.workspace = r"C:\GISc450\ArcPy2\Corvallis.gdb"
    workspace = r"C:\GISc450\ArcPy2"

    folder_out = "Strobel_data"
    folder_out_location = os.path.join(workspace, folder_out)

    print(f"\nShapefiles will be written to {folder_out}")

    # Creating the new Strobel_data folder

    if os.path.exists(folder_out_location):
        shutil.rmtree(folder_out_location)
        os.makedirs(folder_out_location)
    else:
        os.makedirs(folder_out_location)

    folder_out_location = os.path.join(workspace, folder_out)

    fc_list = arcpy.ListFeatureClasses()

    # Examining the features in the Corvallis GDB

    for features in fc_list:
        desc = arcpy.Describe(features)
        shape_type = desc.shapeType
        fc_name = desc.name
        get_count = arcpy.GetCount_management(features)
        count = int(get_count.getOutput(0))

    # Assigning new feature names based on our shape type and number of records

        if count <= 1000 and shape_type == "Point":
            name = fc_name + "PointL"
        elif count >= 1001 and shape_type == "Point":
            name = fc_name + "PointM"
        elif count <= 1000 and shape_type == "Polyline":
            name = fc_name + "PolylineL"
        elif count >= 1001 and shape_type == "Polyline":
            name = fc_name + "PolylineM"
        elif count <= 1000 and shape_type == "Polygon":
            name = fc_name + "PolygonL"
        elif count >= 1001 and shape_type == "Polygon":
            name = fc_name + "PolygonM"

    # Printing the feature information and moving them to the Strobel_data folder

        arcpy.FeatureClassToFeatureClass_conversion(features, folder_out_location, name)
        print(f"\n{features} is a {shape_type} feature class containing {count} record(s)")
        print(f"under the name {name}")

    print(f"\nThe features have been moved to {folder_out}")

    # Counting the number of features examined

    num_features = len(fc_list)
    print(f"\nThere were {num_features} features examined")


if __name__ == '__main__':
    main()

# Timing the script run time

time_end = time.time()
total_time = time_end - time_start
minutes = int(total_time / 60)
seconds = total_time % 60
print(f"\nThe script finished in {minutes} minutes {int(seconds)} seconds")
