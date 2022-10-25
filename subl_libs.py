import os
import shutil





def zalohuj (SYNC_FOLDER, SOURCE):
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