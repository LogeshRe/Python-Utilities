# This program prints the list of all Excel files in a choosen directory and all its sub-directory's.
# Run the program and choose the folder. It will print out all .xls files in the choosen folder and all its sub_folders

from os import listdir
import os

def Readpath():
    from tkinter.filedialog import askdirectory
    foldername = askdirectory()
    return foldername

def xlfinder(original_folder):
    list_of_files = listdir(original_folder)
    list_of_xl_files = []
    child_list_of_xl_files = []
    for name in list_of_files:
        new_path = original_folder + '/' + name
        if(os.path.isdir(new_path)):
            temp_list = xlfinder(new_path)
            if(temp_list != []):
                child_list_of_xl_files.extend(temp_list)
        else:
            if(name[-4:]=='.xls'):
                list_of_xl_files.append(name)

    if(child_list_of_xl_files != []):
        list_of_xl_files.extend(child_list_of_xl_files)

    return list_of_xl_files

original_folder = Readpath()
for name in xlfinder(original_folder):
    print(name)



    
