'''
#!/usb/bin/env python3
'''
import psutil
import shutil


def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    #print(usage)
    if usage >= percent:
        message = 'Error - CPU usage is over {}%'.format(usage)
    else:
        message = 'Everything is OK'

    return message

if __name__ == "__main__":
    percent = 80
    message = check_cpu_usage(percent)
    print(message)

'''
if not check_cpu_usage(80):
    print("Error - CPU usage is over 80%")
else:
    print("Everything ok")
'''