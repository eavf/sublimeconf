

out1 = os.path.isdir(SOURCE)
out2 = os.path.isdir(SYNC_FOLDER)
print("SOURCE:      ", out1)
print("SYNC_FOLDER: ", out2)

now = datetime.datetime.now()

DROPBOX="$HOME/Dropbox"

# Where do we put Sublime settings in our Dropbox
SYNC_FOLDER="$DROPBOX/IT/sublimetext"

# Where Sublime settings have been installed
meno=$(uname)
echo "$meno"

fi

# Check that settings really exist on this computer
if [ ! -e "$SOURCE/Packages/" ]; then
        echo "Could not find $SOURCE/Settings/"
        exit 1
fi

# Detect that we don't try to install twice and screw up
if [ -L "$SOURCE/Packages" ] ; then
        echo "Dropbox settings already symlinked"
        exit 1
fi

# XXX: Disabled Settings/ folder syncing as looks like
# Sublime keeps only license and .sublime_session files -
# the latter
# which are autosaved and would cause unnecessary conflicts
# and traffic
echo "$SYNC_FOLDER/Installed Packages"





        # Dropbox has not been set-up on any computer before?
        if not (os.path.isdir(SYNC_FOLDER)):
                if syncovanafld():
                        # Copy the files into their respective folder

                        shutil.copytree(SOURCE, SYNC_FOLDER, ignore = ignoreFunc('a'))
        else:
                shutil.copytree(SOURCE, SYNC_FOLDER)












# Now when settings are in Dropbox delete existing files
##rm -rf "$SOURCE/Installed Packages"
##rm -rf "$SOURCE/Packages"
#rm -rf "$SOURCE/Settings"

# Symlink settings folders from Drobox
# The "Installed Packages" and "Packages" was never
# created inside of Dropbox folder. These lines are not working.
# Fixed to the correct folder.

##ln -s "$SYNC_FOLDER/Installed Packages" "$SOURCE/Installed Packages"
##ln -s "$SYNC_FOLDER/Packages" "$SOURCE/Packages"
#ln -s "$SYNC_FOLDER/Settings" "$SOURCE/Settings"
###
