import os
import random
import ctypes
import ntpath

# select a random file from the directory assigned to dir
dir = 'D:\\Sean\\Pictures\\HD Wallpapers\\1080'
filename = random.choice(os.listdir(dir))
#path = os.path.join(dir, filename)
#path = ntpath.join(dir, filename)
path = dir + '\\' + filename

# test to see if the first part is working
'''f1 = open('C:/Users/Sean/Desktop/selection.txt', 'w+')
f1.truncate(0)
f1.write(path)
f1.close'''

# set the selected file as the wallpaper
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r'D:\Sean\Pictures\HD Wallpapers\1080\500822.jpg' , 0)