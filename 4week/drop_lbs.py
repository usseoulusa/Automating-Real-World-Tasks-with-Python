'''
#!/usr/bin/env python3
'''

string = "500 lbs"
print(string) # 500 lbs
separated = ''.join(string).split()
print(separated) # ['500', 'lbs']
string = separated[0]
print(type(string), string) # <class 'str'> 500
now_num = int(string)
print(type(now_num), now_num) # <class 'int'> 500


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

data = {'name':'mango', 'weight':500, 'description':'delicious'}
data["image_name"] = "001.jpeg"
print(data) # {'name': 'mango', 'weight': 500, 'description': 'delicious', 'image_name': '001.jpeg'}