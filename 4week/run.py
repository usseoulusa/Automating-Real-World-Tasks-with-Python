'''
#!/usr/bin/env python3
'''

import os
#import requests

path = "/data/feedback/"

#path = "c://a_Python//a_google_course//a_final_project//2week//feedback//"
#save_path = "c://a_Python//a_google_course//a_final_project//2week//feedback//"

dir_list = os.listdir(path)
#print(dir_list)

# to store files in a list
list = []
# to store feedback content in a dictionary
content = {}
# to store each line in a list
line_list = []
# keywords for content dictionary
keywords = ["name", "weight", "description", "image_name"]

# Challenge
# Description text has 3 lines: "name", "weight", description"
# How to add fourth keyword "image_name"?
# Proposal1: generate image list and add to dictionary for matching fruit
# Proposal2: generate dictionary of description file and matching image
#
# Eureka! - Add keyword and value to the existing dictionary
#content = {"name": "001.txt", "weight": 500, "description": "delicious"}
#content["image_name"] = "001.jpeg"
#print(content)
#{"name": "001.txt", "weight": 500, "description": "delicious", "image_name": "001.jpeg"}

images_list = ["001.jpeg", "002.jpeg", "003.jpeg", "004.jpeg", "005.jpeg",
               "006.jpeg", "007.jpeg", "008.jpeg", "009.jpeg", "010.jpeg"]

# Challenge
# weight is in the form of "500 lbs"
# "500 lbs" must be changed to integer "500"
# Proposal: 1. drop lbs 2. int("string number")

def get_dictionary(file):
    content = {}
    with open(file) as f:
        i = 0
        for line in f:
            line = line.rstrip()
            # Strip lbs and turn to integer
            if i == 1:
                separated = ''.join(line).split()
                string = separated[0]
                now_num = int(string)
                line = now_num
            #line_list.append(line)
            content[keywords[i]] = line

            # Final thought:
            # Adding image_list did not work
            # I ended up image file name for each item(txt file) at the end,
            # so when I convert to dictionary, it picked up image_list file 
            content["image_name"] = images_list[i]
            i += 1
            # Add image_name
            # How?
            #if i == 3:
            #    content[keywords[i]] = images_list[what here?]
    return content

def get_list_dictionary(dir_list):
    list = []
    for feedback in dir_list:
        dict = get_dictionary(feedback)
        list.append(dict)
    return list

def publish(data_serial):
    #response = requests.post("http://34.27.210.59/feedback", json=data_serial)

    for each in data_serial:
        #print(each)
        #response = requests.get('http://34.27.210.59')

        #*****
        # URL must end with a slash "http://34.27.210.59/feedback" error
        # Found out by printing response.text and read through
        response = requests.post("http://34.27.49.107/feedback/", json=each)
        print(response.text)
        #if not response.ok:
        #    raise Exception("GET failed with status code {}".format(response.status_code))
        #else:
        #    print(response.status_code)

data_serial = get_list_dictionary(dir_list)
publish(data_serial)


#print(data_serial)
#print(dict)
#print(list)


'''
for feedback in dir_list:
    print(feedback)
    
    with open(feedback) as f:
        i = 0
        for line in f:
            line = line.rstrip()
            #line_list.append(line)
            content[keywords[i]] = line
            i += 1

            #print(line)
            #content["title"] = line_list[0]
            #content["name"] = line_list[1]
            #content["date"] = line_list[2]
            #content["feedback"] = line_list[3]
        list.append(content)
    
#print(content)
print(list)
#print(line_list)
'''