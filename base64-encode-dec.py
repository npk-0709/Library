import base64

string_='python' #input

#script execute with code ascii

code='ascii'

string_encoded=base64.b64encode(string_.encode(code)).decode(code)

print(string_encoded)# print code encoded


#*********************************************************************


# decode with python 

string_='cHl0aG9u'  ## input

#script execute with code ascii

code='ascii'

string_decoded=base64.b64decode(string_.encode(code)).decode(code)

print(string_decoded) #print decoded
