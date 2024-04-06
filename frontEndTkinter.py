from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory
import tkinter as tk
import sys

#https://docs.python.org/3.10/library/tkinter.messagebox.html
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



        submitLabel = ttk.Label(self.mainWindow, text= "Once options are selected, click Submit.")
        submitLabel.place(x=180, y=275)
        self.submitButton = ttk.Button(self.mainWindow, text="Submit", command=self.submitSelection)
        self.submitButton.place(x=250, y=300)        
        
        #Input filepath choice
        self.inputButton = ttk.Button(self.mainWindow, text = 'Input Directory', command=self.selectInputDirectory)
        self.inputButton.place(x=100,y=100)
        self.inputPathLabel = ttk.Label(self.mainWindow, text = 'No input directory selected')
        self.inputPathLabel.place(x=100, y=125)

        #Output filepath choice
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