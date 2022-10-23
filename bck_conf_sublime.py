import os, platform
import sys
import pprint
import shutil


def zalohuj ():
        try:
                print ("Zalohuj: ", SYNC_FOLDER)
                if os.path.exists(SYNC_FOLDER):
                        shutil.rmtree(SYNC_FOLDER)
                shutil.copytree(SOURCE, SYNC_FOLDER)
        except OSError as e:
                print(e)

def create_folder_struct ():
        #Nakoneic netreba, lebo kopirujeme všetko
        print("Setting up Dropbox sync folder, it does not exists.....")

         # Creating the folders in separated categories
        print ("$SYNC_FOLDER/Installed Packages")
        PATH = os.path.join(SYNC_FOLDER, 'Installed Packages')
        os.makedirs(PATH, exist_ok=True)
        PATH = os.path.join(SYNC_FOLDER, 'Packages')
        os.makedirs(PATH, exist_ok=True)
        PATH = os.path.join(SYNC_FOLDER, 'Settings')
        os.makedirs(PATH, exist_ok=True)
        return True


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
                home = os.environ['HOME']
                SOURCE = os.path.join(home, folder_name)
                print ("Whole path to configuration is : ", SOURCE)
                ano = input("Is that correct (y/n)")
        #SOURCE="$HOME/AppData/Roaming/Sublime Text 3"

        DROPBOX=os.path.join(home, "Dropbox")
        SYNC_FOLDER=os.path.join(DROPBOX, "IT/sublimetext")
        #zalohuj()

elif platforma[0] == "Linux":
        home = os.environ['HOME']
        SOURCE = os.path.join(home, '.config', 'sublime-text')
        #SOURCE="$HOME/.config/sublime-text"
        print("Source is: ", SOURCE)
        # Where do we put Sublime settings in our Dropbox
        DROPBOX=os.path.join(home, "Dropbox")
        SYNC_FOLDER=os.path.join(DROPBOX, "IT", "sublimetext", f'{platforma[0]}')
        print("Syncdir is: ",SYNC_FOLDER)
        #Suzalohuj()

else:
        print("Unknown operating system")
