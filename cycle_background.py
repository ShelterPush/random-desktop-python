import os
import random
import ctypes
#import ntpath

# select a random file from the directory assigned to dir
#dir = 'directory_of_interest'  # For example,
dir = 'D:\\ShelterPush\\Pictures\\HD Wallpapers\\1080' # The double backslashes are required for Python and Windows
filename = random.choice(os.listdir(dir)) # Chooses a random file from within that directory
#path = os.path.join(dir, filename) # constantly produced forward slashes instead of back slashes
#path = ntpath.join(dir, filename)  # same
path = dir + '\\' + filename        # kind of hacky, but it works

# test to see if the first part is working
'''f1 = open('C:/temp/selection.txt', 'w+')
f1.truncate(0)
f1.write(path)
f1.close'''

# set the selected file as the wallpaper
SPI_SETDESKWALLPAPER = 20 # honestly not sure why 20, but I'm sure the documentation for SPI_SETDESWALLPAPER explains it
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r'D:\Sean\Pictures\HD Wallpapers\1080\500822.jpg' , 0) # This is just a test
