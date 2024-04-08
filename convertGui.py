# Add geopackages reading to it better formatted so that tables can be added. Will need a specific part of the loop.
# Add driver as a choosable input - done
# Add option to select which files or which depends which files are in the folder so it doesn't discriminate.
# Make it so it can change 'any OGR file to any other OGR file'.

import sys
# For GUI
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import tkinter as tk

from batchConvertMethod import batchConvert

# ---- GUI Class definition ----
class convertGui:
    def __init__(self):
        # dict of formats to convert to and from with their file extension
        # Print supported drivers and their capabilities
        self.driverOptionsDict = {
            'DXF': '.dxf', 'CSV': '.csv', 'OpenFileGDB': '.gdb',  'ESRIJSON': '.json', 'ESRI Shapefile': '.shp', 
            'FlatGeobuf': '.fgb', 'GeoJSON': '.geojson', 'GeoJSONSeq': '.geojsons', 'GPKG': '.gpkg', 'GML': '.gml',
            'OGR_GMT': '.GMT', 'GPX': '.gpx', 'Idrisi': '.rst', 'MapInfo File': '.tab',
            'DGN': '.dgn', 'PCIDSK': '.pix',  'S57': '.000', 'SQLite': '.sqlite', 'TopoJSON': '.topojson'
            }
        self.crsOptions = [
            "EPSG:25832 - ETRS89 / UTM zone 32N (Europe)",
            "EPSG:27700 - OSGB36 (OS Great Britain 1936)",
            "EPSG:29902 - TM65 / Irish Grid"
            "EPSG:32633 - WGS 84 / UTM zone 33N",
            "EPSG:32736 - WGS 84 / UTM zone 36S",
            "EPSG:3857 - WGS 84 / Pseudo-Mercator",         
            "EPSG:4258 - ETRS89 / Europe",         
            "EPSG:4269 - NAD83 (North American Datum 1983)",
            "EPSG:4326 - WGS 84 (Global GPS Coordinate System)",

        ]
        
        self.driverOptions = list(self.driverOptionsDict.keys())
        self.conversionCrs = ''  # for use in batchConvert from interface choice

        # gui main window holding variables
        self.mainWindow = tk.Tk() # usually called root in examples. This is the main window.
        self.conversionUI()

        # main window UI of tkinter for conversion tool
    def conversionUI(self):
        self.mainWindow.config(width=800, height=500)
        self.mainWindow.title('GIS File Conversion')

        # Input conversion file type
        comboInputLabel = ttk.Label(self.mainWindow, text = "Convert from:")
        comboInputLabel.place(x=100, y=25)
        self.comboInput = ttk.Combobox(
            state="readonly",
            values= self.driverOptions
        )
        self.comboInput.place(x=100, y=50)

        # Conversion (convert to) file type
        comboConvertLabel = ttk.Label(self.mainWindow, text="Convert to:")
        comboConvertLabel.place(x=450, y=25)
        self.comboConvert = ttk.Combobox(
            state='readonly',
            values=self.driverOptions
        )
        self.comboConvert.place(x=450,y=50)

        # CRS conversion drop down menu
        crsComboLabel = ttk.Label(self.mainWindow, text='Output CRS:')
        crsComboLabel.place(x=450, y=100)
        self.comboCrs = ttk.Combobox(
            state = 'readonly',
            values=self.crsOptions
        )
        self.comboCrs.place(x=450, y=125)

        # Submit button - very important to making it all run beyond this.
        submitLabel = ttk.Label(self.mainWindow, text= "Once options are selected, click Submit.")
        submitLabel.place(x=280, y=225)
        self.submitButton = ttk.Button(self.mainWindow, text="Submit", command=self.submitSelection)
        self.submitButton.place(x=350, y=250)        

        # Input filepath button choice with dynamic path label
        self.inputButton = ttk.Button(self.mainWindow, text = 'Input Directory', command=self.selectInputDirectory)
        self.inputButton.place(x=100,y=100)
        self.inputPathLabel = ttk.Label(self.mainWindow, text = 'No input directory selected')
        self.inputPathLabel.place(x=100, y=125)

        # Output filepath choice with dynamic path label
        self.outputButton = ttk.Button(self.mainWindow, text='Output Directory', command=self.selectOutputDirectory)
        self.outputButton.place(x=100, y=175)
        self.outputPathLabel = ttk.Label(self.mainWindow, text='No output directory selected')
        self.outputPathLabel.place(x=100, y=200)

    # for select input directory button.
    def selectInputDirectory(self):
        self.inputPath = askdirectory(title='Select Input Directory')
        # dynamically shows input directory
        if self.inputPath:
            self.inputPathLabel.config(text=self.inputPath)

    # for select output directory button.
    def selectOutputDirectory(self):
        self.outputPath = askdirectory(title="Output directory for converted files")
        # dynamically shows output directory if one is selected
        if self.outputPath:
            self.outputPathLabel.config(text=self.outputPath)

    def submitSelection(self):
        # use .get() to get the selected value from combobox
        messageBoxInput = messagebox.askyesnocancel(title = 'Confirmation', message='Do you want to submit?')
        if messageBoxInput == True:
            # Returns conversion Driver and then returns the extension from dict based on that value
            self.conversionDriver = self.comboConvert.get()
            self.conversionDriverExt = self.driverOptionsDict.get(self.conversionDriver)
            # Returns input Driver and then returns extension
            self.inputDriver = self.comboInput.get()
            self.inputDriverExt = self.driverOptionsDict.get(self.inputDriver)
            # extracts just the EPSG value from the list. creates list of 2, fetches number.
            self.conversionCrs =self.comboCrs.get().split('-')[0].split(':')[1].strip()
            #Conversion calls batchConvert.py
            messagebox.showinfo(title = 'Conversion Tool', message='Conversion going ahead!')
            batchConvert(self)
        # If select No -> False -> closes everything and stops script.
        elif messageBoxInput == False:
            self.mainWindow.destroy()
            messagebox.showinfo(title= 'Conversion Tool', message='Conversion tool ended.')
            sys.exit()
        # If select Cancel -> None -> lets user continue and change settings.

    def run(self):
        self.mainWindow.mainloop()
# Run the gui to input.
convertFrontEnd = convertGui()
convertFrontEnd.run()

# Once submit clicked, run the batch convert.


