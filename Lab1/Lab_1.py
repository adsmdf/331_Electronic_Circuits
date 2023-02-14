#2/7/2023
#Importing the libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from tkinter import filedialog

#%% Functions
#%% Start Code
#Closing plots before running again
plt.close('all')

#Select Data Frame
folder_path = r'C:\Users\adsmdf\Master Folder\Python\D-Dot Parser\Master Data Folder' #Change this to your folder path
file_path = filedialog.askopenfilename(initialdir=folder_path)
data = pd.read_excel(file_path) #Make sure you use .xlsx files not .csv!

#%%Setting data variables
time = data['time']
C1 = data['C1'] #Make sure to change the column name to match the data
C2 = data['C2'] #Make sure to change the column name to match the data
M1 = data['M1'] #Make sure to change the column name to match the data

#%%Plotting
# fig1, ax1 = plt.subplots()
# ax1.plot(time, C2)
# ax1.set_title('C2 vs Time')
# ax1.set_xlabel('Time (s)')
# ax1.set_ylabel('C2 (V)')
# ax1.grid()


# fig2, ax2 = plt.subplots()
# ax2.plot(time, C1)
# ax2.set_title('C1 vs Time')
# ax2.set_xlabel('Time (s)')
# ax2.set_ylabel('C1 (V)')
# ax2.grid()

# fig3, ax3 = plt.subplots()
# ax3.plot(C1,np.log10(M1))
# ax3.set_title('C1 vs M1')
# ax3.set_xlabel('C1 (V)')
# ax3.set_ylabel('M1 (I)')
# ax3.grid()

#%%Skipping data
#LN271
# timel = time[300:1000]
# C1l = C1[300:1000]
# C2l = C2[300:1000]
# M1l = M1[300:1000]

#LN4001
timel = time[5216:8001]
C1l = C1[5216:8001]
C2l = C2[5216:8001]
M1l = M1[5216:8001]
#Check text from Nathaniel for ranges to try
#%%Plotting
# fig4, ax4 = plt.subplots() #plt = class 
# ax4.plot(timel, C2l)
# ax4.set_title('C2 vs Time')
# ax4.set_xlabel('Time (s)')
# ax4.set_ylabel('C2 (V)')
# ax4.grid()

# fig5, ax5 = plt.subplots()
# ax5.plot(timel, C1l)
# ax5.set_title('C1 vs Time')
# ax5.set_xlabel('Time (s)')
# ax5.set_ylabel('C1 (V)')
# ax5.grid()

fig6, ax6 = plt.subplots()
ax6.plot(np.polyfit(C1l,np.log10(M1l),1))
ax6.set_title('Polyfit Graph')
ax6.set_xlabel('C1 (V)')
ax6.set_ylabel('M1 (I)')
ax6.grid()

# fig7, ax7 = plt.subplots()
# ax7.plot(np.log10(M1l),C1l)
# ax7.set_title('M1 vs C1')
# ax7.set_xlabel('M1 (I)')
# ax7.set_ylabel('C1 (V)')
# ax7.grid()