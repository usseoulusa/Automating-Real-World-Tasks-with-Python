'''
#!/usr/bin/env python
'''

import os
from PIL import Image


path = "c://a_Python//a_google_course//a_final_project//1week//images"
dir_list = os.listdir(path)

#print(dir_list)

# to store files in a list
list = []

 
''' Requirement
1. Iterate through each file in the folder

2. For each file:
    a. Rotate the image 90° clockwise
    b. Resize the image from 192x192 to 128x128
    c. Save the image to a new folder in .jpeg format
'''
for (root, dirs, file) in os.walk(path):
    for f in file:
        
        #print(f)
        #if '.tiff' in f:
            #print(f)
