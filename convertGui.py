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

from batchconvert import batch_convert


# ---- GUI Class definition ----
class ConvertGui:
    def __init__(self):
        # dict of formats to convert to and from with their file extension
        # Print supported drivers and their capabilities
        self.driver_options_dict = {
            'DXF': '.dxf', 'CSV': '.csv', 'OpenFileGDB': '.gdb',  'ESRIJSON': '.json', 'ESRI Shapefile': '.shp', 
            'FlatGeobuf': '.fgb', 'GeoJSON': '.geojson', 'GeoJSONSeq': '.geojsons', 'GPKG': '.gpkg', 'GML': '.gml',
            'OGR_GMT': '.GMT', 'GPX': '.gpx', 'Idrisi': '.rst', 'MapInfo File': '.tab',
            'DGN': '.dgn', 'PCIDSK': '.pix',  'S57': '.000', 'SQLite': '.sqlite', 'TopoJSON': '.topojson'
            }
        self.driver_options = list(self.driver_options_dict.keys())

        self.crs_options_dict = {
            'ETRS89 / UTM Zone 32N (Europe) - EPSG: 25832': '25832',
            'OSGB36 (OSGB 1936) - EPSG: 27700': '27700',
            'TM65 / Irish Grid - EPSG: 29902': '29902',
            'WGS 84 / UTM Zone 33N - EPSG: 32633': '32633',
            'WGS 84 / UTM Zone 36S - EPSG: 32736': '32736',
            'WGS 84 / Pseudo-Mercator - EPSG: 3857': '3857',
            'ETRS89 / Europe - EPSG: 4258': '4258',
            'NAD83 (North American Datum 1983) - EPSG: 4269': '4269',
            'WGS 84 (Global GPS Coordinate System) - EPSG: 4326': '4326'
            }
        
        self.crs_options = list(self.crs_options_dict.keys())
        self.conversion_crs = ''  # for use in batchConvert from interface choice

        # gui main window holding variables
        self.main_window = tk.Tk() # usually called root in examples. This is the main window.
        self.conversion_ui()

        # main window UI of tkinter for conversion tool
    def conversion_ui(self):
        self.main_window.config(width=800, height=500)
        self.main_window.title('GIS File Conversion')

        # Input conversion file type
        combo_input_label = ttk.Label(self.main_window, text = "Convert from:")
        combo_input_label.place(x=100, y=25)
        self.combo_input = ttk.Combobox(
            state="readonly",
            values= self.driver_options
        )
        self.combo_input.place(x=100, y=50)

        # Conversion (convert to) file type
        combo_convert_label = ttk.Label(self.main_window, text="Convert to:")
        combo_convert_label.place(x=450, y=25)
        self.combo_convert = ttk.Combobox(
            state='readonly',
            values=self.driver_options
        )
        self.combo_convert.place(x=450,y=50)

        # CRS conversion drop down menu
        crs_combo_label = ttk.Label(self.main_window, text='Output CRS:')
        crs_combo_label.place(x=450, y=100)
        self.combo_crs = ttk.Combobox(
            state = 'readonly',
            values=self.crs_options
        )
        self.combo_crs.place(x=450, y=125)

        # Submit button - very important to making it all run beyond this.
        submit_label = ttk.Label(self.main_window, text= "Once options are selected, click Submit.")
        submit_label.place(x=280, y=225)
        self.submit_button = ttk.Button(self.main_window, text="Submit", command=self.submit_selection)
        self.submit_button.place(x=350, y=250)        

        # Input filepath button choice with dynamic path label
        self.input_button = ttk.Button(self.main_window, text = 'Input Directory', command=self.select_input_directory)
        self.input_button.place(x=100,y=100)
        self.input_path_label = ttk.Label(self.main_window, text = 'No input directory selected')
        self.input_path_label.place(x=100, y=125)

        # Output filepath choice with dynamic path label
        self.output_button = ttk.Button(self.main_window, text='Output Directory', command=self.select_output_directory)
        self.output_button.place(x=100, y=175)
        self.output_path_label = ttk.Label(self.main_window, text='No output directory selected')
        self.output_path_label.place(x=100, y=200)
        
        

    # for select input directory button.
    def select_input_directory(self):
        self.input_path = askdirectory(title='Select Input Directory')
        # dynamically shows input directory
        if self.input_path:
            self.input_path_label.config(text=self.input_path)

    # for select output directory button.
    def select_output_directory(self):
        self.output_path = askdirectory(title="Output directory for converted files")
        # dynamically shows output directory if one is selected
        if self.output_path:
            self.output_path_label.config(text=self.output_path)

    def submit_selection(self):
        # use .get() to get the selected value from combobox
        message_box_input = messagebox.askyesnocancel(title = 'Confirmation', message='Do you want to submit?')
        if message_box_input == True:
            # Returns conversion Driver and then returns the extension from dict based on that value
            self.conversion_driver = self.combo_convert.get()
            self.conversion_driver_ext = self.driver_options_dict.get(self.conversion_driver)
            # Returns input Driver and then returns extension
            self.input_driver = self.combo_input.get()
            self.input_driver_ext = self.driver_options_dict.get(self.input_driver)
            # extracts just the EPSG value from the dict.
            self.conversion_choice = self.combo_input.get()
            self.conversion_crs = self.crs_options_dict.get(self.conversion_choice)
            
            #Conversion calls batchConvert.py
            messagebox.showinfo(title = 'Conversion Tool', message='Conversion going ahead!')
            #-----Run the batch convert tool after updating all the vars------
            batch_convert(self.input_path, self.output_path, self.input_driver, self.input_driver_ext, self.conversion_driver, self.conversion_driver_ext, self.conversion_crs)
            messagebox.showinfo(title = 'Conversion Tool', message = 'Conversion complete!')
        # If select No -> False -> closes everything and stops script.
        elif message_box_input == False:
            messagebox.showinfo(title= 'Conversion Tool', message='Conversion tool ended.')
        # If select Cancel -> None -> lets user continue and change settings.

    def run(self):
        self.main_window.mainloop()
# Run the gui to input.
convertFrontEnd = ConvertGui()
convertFrontEnd.run()

# Once submit clicked, run the batch convert.



