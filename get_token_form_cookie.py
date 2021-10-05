import requests
_cookie="sb=L5NIYa_jXoIuW5h0DgoBt37w; datr=L5NIYfYjnF1oRnNBcqQCmzTm; _fbp=fb.1.1632277778648.416784890; locale=vi_VN; dpr=1; wd=1304x697; c_user=100029745455196; spin=r.1004498018_b.trunk_t.1633393944_s.1_v.2_; xs=47%3A1hVM2bXTD5v1pA%3A2%3A1633393941%3A-1%3A6265%3A%3AAcUhW7AxyvV_p-JoHVW3MKUk6rkzXX6jIqvqwQM3dQ; fr=0XnYm3jAr0eMfSA1Z.AWWY_Aml8Q2x_FbS9kqmPz2-5po.BhW7-w.HI.AAA.0.0.BhW7-w.AWUTl1lzudM"
headers={
    "Connection": "keep-alive",
    "Keep-Alive": "300",
    "authority":"m.facebook.com",
    "accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
    "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"max-age=0",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site":"none",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "cookie":_cookie,
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",

}
data=requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed",headers=headers).text
token=data.split(f'\\"accessToken\\":\\"')[1].split(f'\\",\\"useLocalFilePreview\\"')[0]
print(token)
