import os
def rename_files():
    #(1) get file names from a folder
    #file_list = os.listdir(r"C:\Users\mwwilcox\Training\Udacity-Python\prank\prank")
    #print(file_list)
    save_path = os.getcwd()
    print ("Current working directory: "+save_path)
    #(2) for each file, rename filename
    #for file_name in file_list:
    #    os.rename(file_name, file_name.translate(None, "0123456879"))

rename_files()
