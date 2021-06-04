import os
import shutil
import time

path = input("Enter the path of the directory/folder/file you want to organize: ")
days = input("Enter the maximum number of days/age for your path: ")
seconds = time.time()-(days*24*60*60)
allFiles = os.listdir(path)

if os.path.exists(path) is True:
    for root_folder, folders, files in os.walk(path):
        if seconds>=getAgeOfPath(root_folder):
            removePath(root_folder)
        else:
            if seconds>=getAgeOfPath(folders):
                removeFolder(folders)

            if seconds>=getAgeOfPath(files):
                removeFile(files)
        
    for file in allFiles:
        name, extension = os.path.splitext(file)
        ext = ext[1:]
        if ext == '':
            continue
        if os.path.exists(path + '/' + ext):
            shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
        
        else:
            if ext == 'py':
                os.makedirs(path + '/' + 'python')
                shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

            if ext == 'txt':
                os.makedirs(path + '/' + 'text')
                shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
            
            if ext == 'js':
                os.makedirs(path + '/' + 'javascript')
                shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
            
            if ext == 'png':
                os.makedirs(path + '/' + 'png_images')
                shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

            if ext == 'jpg':
                os.makedirs(path + '/' + 'jpg_images')
                shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

                
else:
    print("Path not found")

def getAgeOfPath(path):
    pathAge = os.stah(path).st_mtime
    return pathAge

def removeFolder(folder):
    folderPathJoined = os.path.join(path + '/' + folder)
    if not os.remove(folderPathJoined):
        print("Folder removed successfully")
    else:
        print("Error: Folder removed unsuccessfully")
    
def removeFile(files):
    filePathJoined = os.path.join(path + '/' + files)
    if not os.remove(filePathJoined):
        print("File removed successfully")
    else:
        print("Error: File removed unsuccessfully")

