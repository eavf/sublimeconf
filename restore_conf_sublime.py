import os, platform
import sys
import pprint
import shutil

def obnov ():
        try:
                if os.path.exists(SYNC_FOLDER):
                        shutil.rmtree(SYNC_FOLDER)
                        shutil.copytree(SOURCE, SYNC_FOLDER)
        except OSError as e:
                print(e)

def syncovanafld ():
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
print(platforma)
print(platforma[1])

# Get the list of user's
# environment variables
env_var = os.environ

# Print the list of user's
# environment variables
#print("User's Environment variable:")
#pprint.pprint(dict(env_var), width = 1)


if platforma[0] == "Darwin":
        home = os.environ['HOME']
        SOURCE = os.path.join(home, 'Library', 'Application Support', 'sublime-text')
        #SOURCE="$HOME/Library/Application Support/Sublime Text 2"

        DROPBOX=os.path.join(home, "Dropbox")
        SYNC_FOLDER=os.path.join(DROPBOX, "IT/sublimetext")
        zalohuj()

elif platforma[0] == "Linux":
        home = os.environ['HOME']
        SOURCE = os.path.join(home, '.config', 'sublime-text')
        #SOURCE="$HOME/.config/sublime-text"
        print("Source is: ", SOURCE)
        # Where do we put Sublime settings in our Dropbox
        DROPBOX=os.path.join(home, "Dropbox")
        SYNC_FOLDER=os.path.join(DROPBOX, "IT/sublimetext")
        print("Syncdir is: ",SYNC_FOLDER)
        zalohuj()

else:
        print("Unknown operating system")

