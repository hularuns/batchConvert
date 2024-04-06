from tkinter import ttk, messagebox
import tkinter as tk
import sys


#https://docs.python.org/3.10/library/tkinter.messagebox.html
class conversionApp:

    def __init__(self):
        self.driverOptions = ["DXF","CSV", "OpenFileGDB", "ESRIJSON", "ESRI Shapefile", "FlatGeobuf", 
    "GeoJSON", "GeoJSONSeq", "GPKG","GML", "OGR_GMT","GPX","Idrisi","MapInfo File",
    "DGN","PCIDSK","OGR_PDS","S57","SQLite","TopoJSON"]
        self.conversionDriver = ''
        self.inputDriver = ''

        self.mainWindow = tk.Tk()
        self.setupUI()




    def setupUI(self):
        self.mainWindow.config(width=400, height=300)
        self.mainWindow.title('GIS File Conversion')

        #Convert to section
        comboConvertLabel = ttk.Label(self.mainWindow, text="Convert to:")
        comboConvertLabel.place(x=200, y=25)
        self.comboConvert = ttk.Combobox(
            state='readonly',
            values=self.driverOptions
        )
        self.comboConvert.place(x=200,y=50)

        comboInputLabel = ttk.Label(self.mainWindow, text = "Convert from:")
        comboInputLabel.place(x=50, y=25)
        self.comboInput = ttk.Combobox(
            state="readonly",
            values= self.driverOptions
        )
        self.comboInput.place(x=50, y=50)

        submitLabel = ttk.Label(self.mainWindow, text= "Once options are selected, click Submit.")
        submitLabel.place(x=90, y=175)
        self.submitButton = ttk.Button(self.mainWindow, text="Submit", command=self.submitSelection)
        self.submitButton.place(x=150, y=200)        

        
    def submitSelection(self):
    
        #use .get() to get the selected value from combobox
        messageBoxInput = messagebox.askyesnocancel(title = 'Confirmation', message='Do you want to submit')
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
 
app = conversionApp()
app.run()
