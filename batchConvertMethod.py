import geopandas as gpd
import os

def batchConvert(guiInput):
    #Handles differently converting to geopackage.
     
    for gisFile in os.listdir(guiInput.inputPath):
        if gisFile.endswith(guiInput.inputDriverExt):
            fullPath = os.path.join(guiInput.inputPath, gisFile)
            gdf = gpd.read_file(fullPath)
            #converts if conversionCrs is true, otherwise won't convert.
            if guiInput.conversionCrs:
                gdf = gdf.to_crs(guiInput.conversionCrs)
            
            # this section converts file type.
            if guiInput.conversionDriver == 'GPKG':
                outputFileName = 'Converted.gpkg' 
                outputFullPath = os.path.join(guiInput.outputPath, outputFileName)
                tableName = os.path.splitext(os.path.basename(gisFile))[0] #obtains file name of each file adding as layer
                #Create or append to geopackage, will change mode depending on if it exists or not.
                gdf.to_file(outputFullPath, layer=tableName, driver = 'GPKG')
                print(f"Converted {gisFile} to {guiInput.conversionDriver} and saved as a table within {outputFileName} with CRS of {guiInput.conversionCrs}")           
            else:
                # file name and path creation
                outputFileName = os.path.splitext(gisFile)[0] + guiInput.conversionDriverExt
                outputFullPath = os.path.join(guiInput.outputPath, outputFileName)
                # Creates and saves converted file 
                gdf.to_file(outputFullPath, driver=str(guiInput.conversionDriver))
                print(f"Converted {gisFile} to {guiInput.conversionDriver} and saved as {outputFileName}")
        


#batchConvert(convertFrontEnd)