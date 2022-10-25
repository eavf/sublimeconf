import os, platform
import sys
import pprint
import shutil
from subl_libs import *




# Declaring the ignore function
def ignoreFunc(file):
        def _ignore_(path, names):

                # List containing names of file
                # that are needed to ignore
                ignored = []

                # check if file in names
                # then add it to list
                if file in names:
                        ignored.append(file)
                return set(ignored)
        return _ignore_


platforma = platform.uname()
#print(platforma)
#print(platforma[1])

# Get the list of user's
# environment variables
env_var = os.environ

# Print the list of user's
# environment variables
#print("User's Environment variable:")
#pprint.pprint(dict(env_var), width = 1)


if platforma[0] != "Darwin":
        ano = "n"
        while ano != "y":
                folder_name = input("Enter name of the foldder where sublime text conf is located in $HOME/AppData/Roaming/:")
                appfoldda = os.environ['APPDATA']
                src_fld = os.path.join(appfoldda, folder_name)
                print ("Whole path to configuration is : ", src_fld)
                ano = input("Is that correct (y/n)")
        #SOURCE="$HOME/AppData/Roaming/Sublime Text 3"

        DROPBOX = os.path.join(r'\\192.168.1.201\perscloud\dropbox')
        sync_fld=os.path.join(DROPBOX, r'IT\sublimetext', f'{platforma[0]}')
        #print (SYNC_FOLDER)
        zalohuj(sync_fld, src_fld)

elif platforma[0] == "Linux":
        home = os.environ['HOME']
        SOURCE = os.path.join(home, '.config', 'sublime-text')
        #SOURCE="$HOME/.config/sublime-text"
        print("Source is: ", SOURCE)
        # Where do we put Sublime settings in our Dropbox
        DROPBOX=os.path.join(home, "Dropbox")
        SYNC_FOLDER=os.path.join(DROPBOX, "IT", "sublimetext", f'{platforma[0]}')
        print("Syncdir is: ",SYNC_FOLDER)
        zalohuj()

else:
        print("Unknown operating system")
