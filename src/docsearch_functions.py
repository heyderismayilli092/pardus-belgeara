from pathlib import Path
import docdatabase
import os


# a function that checks the status of the database in the system
def check_database():
    homefolder = Path.home()
    dbpath = homefolder / ".cache" / "pardus-docsearch"  # location where the database will be placed
    if not os.path.exists(dbpath):
      os.makedirs(dbpath)
    os.chdir(dbpath)
    docdatabase.init_storage(dbpath / "docdatabase.db")  # a database is being created at the specified location


# a function that lists all files on the computer
def files_list():
    homefolder = Path.home()

    flist = []
    formats = [".txt", ".pdf"]

    for file in homefolder.rglob("*"):
        file_dir = file.parts  # get file paths
        if any(folder in file_dir for folder in [".local", ".cache"]):  # if the necessary files on the system are outside the user's workspace (.local and .cache), ignore them
            continue
        if file.is_file() and file.suffix.lower() in formats:  # files are added to the list if they match the found file type and include the specified formats
            flist.append(str(file))

    return flist

