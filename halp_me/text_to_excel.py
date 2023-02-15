import pandas as pd
import numpy as np
import glob as glob
import os 
import re 
"""
Step 1:
    - Open the folder with the text files

Step 2:
    - Read the text files into a list of dataframes
    
Step 3:
    - Save the dataframes as excel files
    
"""


def convert_to_excel( file_path):
    os.chdir(file_path)
    sim_text_files = glob.glob( '*' )
    data_list = []
    for i, file in enumerate(sim_text_files):
        data = pd.read_csv( file, sep='\t', header=None, names=['time','voltage'] )
        data.to_excel( file+'.xlsx', index=False )
        data_list.append(data)
        
    return data_list

    # data = pd.read_csv( file_path, sep='\t', header=None, names=['Time','Voltage'] )
    # data.to_excel( file_path+'.xlsx', index=False )
    # return data

def get_all_excel_files( folder_path ):
    os.chdir( folder_path )
    excel_files = glob.glob( '*.xlsx' )
    return excel_files

def convert_to_df( file_path ):
    data = pd.read_excel( file_path )
    return data

if __name__ == '__main__':
    
    #convert text to excel
    sim_data_dir = '/HalfWave/SIM_Data/'
    cwd = os.getcwd()
    print(cwd)
    sim_folder = cwd + sim_data_dir

    #convert text to excel
    data = convert_to_excel(sim_folder)
    
    
    #changes to directory with text files
    os.chdir( cwd+sim_data_dir)
    sim_text_files = glob.glob( '*' )
    sim_excel = get_all_excel_files(sim_folder)
    sim_data_list = []
    
    key_names = ['NOCAP', '47', '100', '10', '147']
    
    sim_data_dictionary = {}
    for excel_file in sim_excel:
        value = re.findall(r'\d+', excel_file)
        #if value is empty then its nocap 
        if not value:
            sim_data_dictionary[key_names[0]] = convert_to_df(excel_file)
            continue 
        
        for key in key_names:
            if key in value:
                print(key, value)
                sim_data_dictionary[key] = convert_to_df(excel_file)
                
        # sim_data_list.append(convert_to_df(excel_file))
    



