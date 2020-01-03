import os

"""
path.join() method from the OS module to concatenate the file name
to its file path,forming an absolute path.
"""

fName = 'Python_Drill.py'
fPath = 'C:\\Users\\Heidi\\Documents\\GitHub\\Python_Projects'
abPath = os.path.join(fPath, fName)
print("Absolute path is: ")
print(abPath)


#Listing all files in directory with listdir() method.

path = os.getcwd()
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :") 
print(dir_list)

"""
getmtime() method from the OS module to find the latest date that each
text file has been created or modified.
"""

import time
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt') :
            thefile = os.path.join(dirname,filename)
            modification_time = os.path.getmtime(filename)
            local_time = time.ctime(modification_time)
            print("Last modification: ", local_time, filename)


"""
print each file ending with a “.txt” file extension and its
corresponding mtime to the console
"""

from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt') :
            thefile = os.path.join(dirname,filename)
            print (os.path.getmtime(thefile), thefile)




