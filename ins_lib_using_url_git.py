import os 
import pyautogui
url=str(pyautogui.prompt("Điền Url Github"))
try:
    url=url.replace("https","git")
except:pass
os.system("color a")
command=f"pip install git+{url}"
os.system("echo Đang Cài Đặt Thư Viện Của Bạn")
os.system(command)
