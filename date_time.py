import time
class time_:
    """hour , minute , second"""
    hour   = time.strftime("%H", time.localtime())
    minute = time.strftime("%M", time.localtime())
    second = time.strftime("%S", time.localtime())