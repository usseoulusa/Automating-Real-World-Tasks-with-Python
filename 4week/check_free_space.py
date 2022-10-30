'''
#!/usb/bin/env python3
'''
import psutil
import shutil


def check_free_space(percent):
    total, used, free = shutil.disk_usage(__file__)
    if free <= percent:
        message = "Error - Available disk space is less than 20%"
    else:
        message = "Everything is OK"
    
    return message

    #return free_space
    #return free_space < percent
if __name__ == "__main__":
    percent = 20
    message = check_free_space(percent)
    print(message)

#if not check_free_space(20):
    #print("Error - Available disk space is less than 20%")
#else:
    #print("Everything ok")