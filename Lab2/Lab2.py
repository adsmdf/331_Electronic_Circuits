#02/14/2023
#Importing the libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from tkinter import filedialog

#%% Start Code
#Closing plots before running again
plt.close('all')

#Select Data Frame
folder_path = r'C:\Users\adsmdf\Master Folder\Python\D-Dot Parser\Master Data Folder' #Change this to your folder path
file_path = filedialog.askopenfilename(initialdir=folder_path)
data = pd.read_excel(file_path) #Make sure you use .xlsx files not .csv!

#%%Setting data variables
# TExp = data['Time']
VEXP = data['Voltage']
# TSim = data['time']
VSim = data['voltage']
#Cutting Data
# TExpC = TExp[0:1000]
VEXPC = VEXP[3938:8192]
# TSimC = TSim[0:1000]
# VSimC = VSim[0:1000]

#%% Min and Max
min(VEXPC)
print (min(VEXPC))
max(VEXPC)
print (max(VEXPC))

min(VSim)
print (min(VSim))
max(VSim)
print (max(VSim))

SIMR = max(VSim) - min(VSim)
EXPR = max(VEXPC) - min(VEXPC)

#%%Plotting
# fig, ax1 = plt.subplots()
# ax1.plot()