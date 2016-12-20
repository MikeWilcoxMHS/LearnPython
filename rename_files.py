import os

photo_directory = ("C:\Users\mwwilcox\Training\Udacity-Python\prank\mymessage")
def rename_files():
    #(1) get file names from a folder
    #file_list = os.listdir(r"C:\Users\mwwilcox\Training\Udacity-Python\prank\prank")
    file_list = os.listdir(photo_directory)
    print(file_list)
    save_path = os.getcwd()
    print ("Current working directory: "+save_path)
    #(2) for each file, rename filename
    os.chdir(photo_directory)
    for file_name in file_list:
        print ("Old file name: "+file_name)
        print ("New file name: "+(file_name.translate(None, "0123456789")))
        os.rename(file_name, file_name.translate(None, "0123456879"))
    os.chdir(save_path)
rename_files()
