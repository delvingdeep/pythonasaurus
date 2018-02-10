import os

#function definition for renaming file
def rename_files():
    #get file names from a folder
    file_list = os.listdir("/Users/deepdoshi/Documents/git/pythonasaurus/2_file_rename_sample")
    print(file_list)

    #for each file, renaming it
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789") )
        
rename_files()
