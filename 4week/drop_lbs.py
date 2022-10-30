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