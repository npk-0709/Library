import time
def get_time():
    hour   = time.strftime("%H", time.localtime())
    minute = time.strftime("%M", time.localtime())
    second = time.strftime("%S", time.localtime())
    return[hour,minute,second]

print(get_time())
