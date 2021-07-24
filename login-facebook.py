
from selenium import webdriver

def __LOGIN_FACEBOOK_WITH_COOKIE_USE_CHROMEDRIVER__(cookie):
    options=webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # off notification
    options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications":2})
    #options.add_argument(f'user-agent={useragent}') # add useragent
    #options.add_argument ("-headless") # hide chrome 
    driver=webdriver.Chrome(options=options)
    driver.set_window_size(800,750) # set size
    driver.get("http://facebook.com") # open tab login facebook
    #script login by javascript and execute
    script='javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + cookie + '"); location.href = "https://facebook.com"; })();'
    driver.execute_script(script) #execute
    return driver # return webdriver 
if __name__=='__main__':
    cookie=' YOUR COOKIE FACEBOOK <F12> :D '
    driver=__LOGIN_FACEBOOK_WITH_COOKIE_USE_CHROMEDRIVER__(cookie)
    
#NPK079-VIETNAM
