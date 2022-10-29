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
 
# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)
        #if '.tiff' in f:
            #print(f)
