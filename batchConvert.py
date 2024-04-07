# Add geopackages reading to it better formatted so that tables can be added. Will need a specific part of the loop.
# Add driver as a choosable input - done
# Add option to select which files or which depends which files are in the folder so it doesn't discriminate.
# Make it so it can change 'any OGR file to any other OGR file'.

import geopandas as gpd
import os
import sys

# These are for folder dialogue prompt
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import tkinter as tk

# ---- GUI Class definition ----
class convertGui:

    def __init__(self):
        self.driverOptions = ["DXF","CSV", "OpenFileGDB", "ESRIJSON", "ESRI Shapefile", "FlatGeobuf", 
    "GeoJSON", "GeoJSONSeq", "GPKG","GML", "OGR_GMT","GPX","Idrisi","MapInfo File",
    "DGN","PCIDSK","OGR_PDS","S57","SQLite","TopoJSON"]
        #output holding variables to be called in batchConvert
        self.conversionDriver = ''
        self.inputDriver = ''
        self.inputPath = ''
        self.outputPath = ''
        #gui main window holding variables
        self.mainWindow = tk.Tk() # usually called root in examples. This is the main window.
        self.setupUI()

        #main window UI of tkinter
    def setupUI(self):
        self.mainWindow.config(width=600, height=400)
        self.mainWindow.title('GIS File Conversion')

        #Conversion (convert to) file type
        comboConvertLabel = ttk.Label(self.mainWindow, text="Convert to:")
        comboConvertLabel.place(x=350, y=25)
        self.comboConvert = ttk.Combobox(
            state='readonly',
            values=self.driverOptions
        )
        self.comboConvert.place(x=350,y=50)
        #Input conversion file type
        comboInputLabel = ttk.Label(self.mainWindow, text = "Convert from:")
        comboInputLabel.place(x=100, y=25)
        self.comboInput = ttk.Combobox(
            state="readonly",
            values= self.driverOptions
        )
        self.comboInput.place(x=100, y=50)
        # Submit button - very important to making it all run beyond this.
        submitLabel = ttk.Label(self.mainWindow, text= "Once options are selected, click Submit.")
        submitLabel.place(x=180, y=275)
        self.submitButton = ttk.Button(self.mainWindow, text="Submit", command=self.submitSelection)
        self.submitButton.place(x=250, y=300)        
        
        #Input filepath button choice with dynamic path label
        self.inputButton = ttk.Button(self.mainWindow, text = 'Input Directory', command=self.selectInputDirectory)
        self.inputButton.place(x=100,y=100)
        self.inputPathLabel = ttk.Label(self.mainWindow, text = 'No input directory selected')
        self.inputPathLabel.place(x=100, y=125)

        #Output filepath choice with dynamic path label
        self.outputButton = ttk.Button(self.mainWindow, text='Output Directory', command=self.selectOutputDirectory)
        self.outputButton.place(x=100, y=175)
        self.outputPathLabel = ttk.Label(self.mainWindow, text='No output directory selected')
        self.outputPathLabel.place(x=100, y=200)

    #for select input directory button.
    def selectInputDirectory(self):
        self.inputPath = askdirectory(title='Select Input Directory')
        #dynamically shows input directory
        if self.inputPath:
            self.inputPathLabel.config(text=self.inputPath)


    #for select output directory button.
    def selectOutputDirectory(self):
        self.outputPath = askdirectory(title="Output directory for converted files")
        #dynamically shows output directory if one is selected
        if self.outputPath:
            self.outputPathLabel.config(text=self.outputPath)

    def submitSelection(self):
    
        #use .get() to get the selected value from combobox
        messageBoxInput = messagebox.askyesnocancel(title = 'Confirmation', message='Do you want to submit?')
        if messageBoxInput == True:
            self.conversionDriver = self.comboConvert.get()
            self.inputDriver = self.comboInput.get()
            self.mainWindow.destroy()
            messagebox.showinfo(title = 'Conversion Tool', message='Conversion going ahead!')
        elif messageBoxInput == False:
            self.mainWindow.destroy()
            messagebox.showinfo(title= 'Conversion Tool', message='Conversion tool ended.')
            sys.exit()

    def run(self):
        self.mainWindow.mainloop()
 
convertFrontEnd = convertGui()
convertFrontEnd.run()

def batchConvert(guiInput):
    #reads gis input file
    gdf = gpd.read_file(fullPath)
    #Handles differently converting to geopackage.
    if convertFrontEnd.conversionDriver == 'GPKG':
                # file name and path creation
        outputFileName = 'Converted.gpkg'
        outputFullPath = os.path.join(guiInput.outputPath, outputFileName)
        for file in os.listdir(guiInput.inputPath):
            if file.endswith(".shp"):
                fullPath = os.path.join(guiInput.inputPath, file)

                tableName = os.path.splitext(os.path.basename(fullPath))[0] #removes directory path for just layer name
                # Creates geopackage, then will append additional layers.
                gdf.to_file(outputFullPath, layer=tableName, driver = 'GPKG')
                print(f"Converted {file} to GeoJSON and saved as {outputFileName}")
    # Select files by just .shp
    # https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    # shape file conversion: https://stackoverflow.com/questions/43119040/shapefile-into-geojson-conversion-python-3
    else:
        for file in os.listdir(guiInput.inputPath):
            if file.endswith(".shp"):
                fullPath = os.path.join(guiInput.inputPath, file)
               # file name and path creation
                outputFileName = os.path.splitext(file)[0] + "." + str(guiInput.conversionDriver)
                outputFullPath = os.path.join(guiInput.outputPath, outputFileName)

                gdf.to_file(outputFullPath, driver=str(guiInput.conversionDriver))

                print(f"Converted {file} to GeoJSON and saved as {outputFileName}")


batchConvert(convertFrontEnd)


