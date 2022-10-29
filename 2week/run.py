'''
#!/usr/bin/env python3
'''


import os
#import requests

path = "c://a_Python//a_google_course//a_final_project//2week//feedback//"
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
keywords = ["title", "name", "date", "feedback"]

def get_dictionary(file):
    content = {}
    with open(file) as f:
        i = 0
        for line in f:
            line = line.rstrip()
            #line_list.append(line)
            content[keywords[i]] = line
            i += 1
    return content

def get_list_dictionary(dir_list):
    list = []
    for feedback in dir_list:
        dict = get_dictionary(feedback)
        list.append(dict)
    return list

def publish(data_serial):
    for each in data_serial:
        print(each)
        #response = requests.post("https://example.com/path/to/api", json=p)
        #if not response.ok:
        #     raise Exception("GET failed with status code {}".format(response.status_code))

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