from tkinter import ttk, messagebox
import tkinter as tk
import sys

conversionDriver = ''
inputDriver = ''
#https://docs.python.org/3.10/library/tkinter.messagebox.html
def submitSelection():
    #access outside variable
    global conversionDriver
    global inputDriver
    #use .get() to get the selected value from combobox

    messageBoxInput = messagebox.askyesnocancel(title = 'Confirmation', message='Do you want to submit')
    if messageBoxInput == True:
        conversionDriver = comboConvert.get()
        inputDriver = comboInput.get()
        mainWindow.destroy()
        messagebox.showinfo(title = 'Conversion Tool', message='Conversion going ahead!')
    elif messageBoxInput == False:
        mainWindow.destroy()
        messagebox.showinfo(title= 'Conversion Tool', message='Conversion tool ended.')

        sys.exit()

driverOptions = ["DXF","CSV", "OpenFileGDB", "ESRIJSON", "ESRI Shapefile", "FlatGeobuf", 
 "GeoJSON", "GeoJSONSeq", "GPKG","GML", "OGR_GMT","GPX","Idrisi","MapInfo File",
 "DGN","PCIDSK","OGR_PDS","S57","SQLite","TopoJSON"]
#Main window
mainWindow = tk.Tk()
mainWindow.config(width=400, height=300)
mainWindow.title('Combobox')

#Convert to section
comboConvertLabel = ttk.Label(mainWindow, text="Convert to:")
comboConvertLabel.place(x=200, y=25)
comboConvert = ttk.Combobox(
    state='readonly',
    values=driverOptions
)
comboConvert.place(x=200,y=50)

comboInputLabel = ttk.Label(mainWindow, text = "Convert from:")
comboInputLabel.place(x=50, y=25)
comboInput = ttk.Combobox(
    state="readonly",
    values= driverOptions
)
comboInput.place(x=50, y=50)

submitLabel = ttk.Label(mainWindow, text= "Once options are selected, click Submit.")
submitLabel.place(x=90, y=175)
submitButton = ttk.Button(mainWindow, text="Submit", command=submitSelection)
submitButton.place(x=150, y=200)
""" button = ttk.Button(text = "Display selection", command=displaySelection)
button.place(x=0, y=0)
 """
mainWindow.mainloop()

print(conversionDriver)
print(f"input {inputDriver}")