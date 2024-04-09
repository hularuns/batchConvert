import geopandas as gpd
import os
import fiona 

def batch_convert(input_path, output_path, input_driver, input_driver_ext, conversion_driver, conversionDriverExt, conversion_crs):
    """Batch Conversion Tool
    Performs batch conversion of GIS files using specified formats and projection.
    
    This function leverages the Fiona library to read, write and append data. Data can be transformed to any EPSG coordinate supported by Fiona.

    Args:
        input_path (str): Directory path for files to be converted.
        output_path (str): Directory path for converted files.
        input_driver (str): Full name in supported driver list by fiona.
        input_driver_ext (str): Driver name Extension (e.g. .shp) (GDAL) of input files. For list, see fiona.supported_drivers.
        cpmversion_driver (str): Driver name (GDAL) to convert to. For list, see fiona.supported_drivers.
        conversion_driver_ext (str): Extension (e.g. .GML) (GDAL) to convert to. see convertGui.driverOptionsDict.
        conversion_crs (int): CRS (EPSG) to reproject to e.g. '4329'. 
    """
    # Handles differently converting to geopackage.

    try:
        for gis_file in os.listdir(input_path):
            if gis_file.endswith(input_driver_ext):
                full_path = os.path.join(input_path, gis_file)
                try:
                    gdf = gpd.read_file(full_path)
                except Exception as error:
                    print(f"Error reading {gis_file}: {error}")
                    continue  # Skip files that cannot be read

                # converts if conversionCrs is true, otherwise won't convert.
                if conversion_crs:
                    gdf = gdf.to_crs(conversion_crs)
                    
                

                # this section converts file type.
                if conversion_driver == 'GPKG':
                    output_file_name = 'Converted.gpkg' 
                    output_full_path = os.path.join(output_path, output_file_name)
                    table_name = os.path.splitext(os.path.basename(gis_file))[0] #obtains file name of each file adding as layer
                    # Create or append to geopackage, will change mode depending on if it exists or not.
                    gdf.to_file(output_full_path, layer=table_name, driver = 'GPKG')
                    print(f"Converted {gis_file} to {conversion_driver} and saved as a table within {output_file_name} with CRS of {conversion_crs}")           
                else:
                    # file name and path creation
                    output_file_name = os.path.splitext(gis_file)[0] + conversionDriverExt
                    output_full_path = os.path.join(output_path, output_file_name)
                    # Creates and saves converted file
                    # Converts to CSV
                    if conversion_driver == 'CSV':
                        gdf.to_csv(output_full_path, index = False, mode='w')
                    # if DXF just use geometries as it only accepts certain specific support fields.
                    elif conversion_driver == "DXF":
                        # extracts only geometry into the gdf for the DXF
                        gdf = gdf[["geometry"]]
                        gdf.to_file(output_full_path, driver=str(conversion_driver))
                    # If any other type:
                    else:
                        gdf.to_file(output_full_path, driver=str(conversion_driver))

                    print(f"Converted {gis_file} to {conversion_driver} and saved as {output_file_name}")
    # should print errors to console
    except Exception as error:
        print(error)                    


# batchConvert(convertFrontEnd)

