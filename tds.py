import os,time,re,json,requests,random
os.system("clear")

print('1\033[92m Add Cookie Facebook')
print('2\033[92m Chạy Tool')
chon=input('\033[93mNhập chế độ bạn chọn ( ví dụ nhập 1hoặc 2): ')
if chon=='1':
	ccccc=open('cookiefb.txt','a')
	tokenfb= input('\033[92mDán Cookie Facebook Vào Đây \033[90m: \033[97m')
	filetokenfb=open('cookiefb.txt','w')
	filetokenfb.write(tokenfb)
	print('\033[92mThành Công , có thể chạy nhiều cookie nhé \033[91m!')
if chon=='2':
	
	tk= input('nhập username :')
	mk=input('nhập password :')
	payload = {"username":tk, "password":mk}
	url = "https://www.traodoisub.com/scr/login.php"
	logintds = requests.post(url, data = payload)
	if logintds.text.find("success") == -1:
		print("\033[91m        [ Tài Khoản Hoặc Mật Khẩu Không Đúng ] ")
		quit()
	else:
		print(" \033[92m       [ Đăng Nhập Thành công Vui Lòng Đợi 1s ]")
		time.sleep(1.5)
	os.system("clear")
	
	data = logintds.headers['Set-Cookie']
	test = re.findall(r'PHPSESSID=[^;]+',data)
	test2 = re.findall(r'__cfduid=[^;]+',data)
	strings11s = ''.join(test)
	strings111s = ''.join(test2)
	keycookietds= strings111s+";"+strings11s
	cookietds = {"cookie" : keycookietds}
	#-------------------Lấy Token------------------------
	kgg= requests.get('https://traodoisub.com/view/setting/', headers = cookietds)
	r2 = re.findall(r'value=.*?readonly=', kgg.text)
	stringx4 = r2[2]
	vietxuokdz = r2[1]
	vietdzok = stringx4.replace('value="', "")
	vietsieudeptrai = vietdzok.replace('" readonly=', "")
	token = vietsieudeptrai
	#print(r2)
	#print(vietsieudeptrai)
	#----------lấy xu---------
	vietxuokdz1 = vietxuokdz.replace('value="', "")
	vietxuokdz2 = vietdzok.replace('" readonly=', "")
	xubaygio = vietxuokdz2
	#all= requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token)
	#xubaygio= all.text.split('')
	print('\033[91m[\033[92m1\033[91m] \033[92m JOB FOLLOW')
	print('\033[91m[\033[92m2\033[91m] \033[92m JOB LIKE PAGE')
	print('\033[91m[\033[92m3\033[91m] \033[92m JOB LIKE POST')
	print('\033[91m[\033[92m4\033[91m] \033[92m RANDOM FOLLOW ALL JOB')
	chonjob= input('\033[93mĐiền Lựa Chọn Của Bạn \033[90m:\033[91m ')
	if chonjob=='1':
		delay = input('\033[93mNhập Delay Giữa Mỗi Job \033[90m:\033[91m ')
		mailll = open('cookiefb.txt','r').read()
		somailll = mailll.split('\n')
		cac = 0
		os.system("clear")
		print('\033[93m--------------------------\033[92m©\033[93m-----------------------------')
		print('\033[1m\033[97m[\033[1m\033[92m ∆ \033[97m] \033[96mCopyright by Mr \033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mMOMO \033[90m:\033[96m0799078754\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mPAYPAL \033[90m:\033[96mofficialbalon2019@gmail.com\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mTELEGRAM \033[90m:\033[96mt.me/mr_a\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mFACEBOOK \033[90m:\033[96mfb.com/danhc.comm\033[92m ☑')
		print('\033[93m══════════════════════════════════════════════════════════')
		while True:
			for cookief1b in somailll:
				r33 = re.findall(r'c_user=.*?;', cookief1b)
				concacc = ''.join(r33)
				concacc = concacc.replace(";", "") 
				idcookie=concacc.split("=")[1]
				cookiefb={'cookie':cookief1b}
				respondse = requests.get("https://mbasic.facebook.com/", headers = cookiefb)
				if respondse.text.find("Đăng xuất") == -1:
					print('\033[97m'+idcookie +'\033[92m | '+'\033[91mCookie Die - Bỏ Qua')
				else:
					laytencookie= requests.get('https://mbasic.facebook.com',headers= cookiefb )
					xuatra = re.findall(r'Đăng xuất .*?<', laytencookie.text)
					tenfbne = ''.join(xuatra)
					tenfbne = tenfbne.replace("Đăng xuất", "") 
					tenfbne = tenfbne.replace("<", "")
					tenfbne1 = tenfbne.replace("(", "") 
					tencookie = tenfbne1.replace(")", "") 
					cauhinhacc= requests.post('https://traodoisub.com/scr/api_dat.php?user='+tk+'&idfb='+idcookie)
					print('\033[97m'+idcookie +'\033[96m|'+ '\033[97m'+tencookie+ '\033[96m|'+'\033[92mTiến Hành Làm ')
					r2= requests.get('https://traodoisub.com/api/?fields=follow&access_token='+token)
					stringx5= r2.text.replace('"','uid')
					stringx4 = re.findall(r': uid.*?uid', stringx5)
					for url1 in stringx4:
						uidfb= url1.split('uid')[1]
						cookiefb={'cookie':cookief1b}
						keyurl= ('https://www.facebook.com/profile.php?id='+uidfb)
						try:
							kq = requests.get(keyurl.replace("www", "mbasic"), headers= cookiefb) 
							rg = re.findall(r'\/a\/subscribe?.*?refid=17', kq.text)
							stringx1 = ''.join(rg)
							stringx3 =  stringx1
							urlfollow = "https://mbasic.facebook.com/"+ stringx3
							urlfollow = urlfollow.replace("amp;", "")
							follow_ok = requests.get(urlfollow, headers = cookiefb)
						except Exception as e:
							print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
							continue
						idfollow= {'id':uidfb}
						cac = int(cac) +1 
						nhanxusub = requests.post("https://www.traodoisub.com/scr/nhantiensub.php", data = idfollow, headers = cookietds)
						if nhanxusub.text.find("2") == -1:
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
						else:
							repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
							r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
							stringx4 = ''.join(r2)
							stringx4 = re.findall(r'>.*?<\/', stringx4)
							stringx5 = ''.join(stringx4)
							stringx5= stringx5.replace("</" , "")
							xubaygio = stringx5.replace(">","")
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
							print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mFOLLOW'+'\033[91m ▶\033[92m+600\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
						time.sleep(int(delay))
	if chonjob=='2':
		delay = input('\033[93mNhập Delay Giữa Mỗi Job \033[90m:\033[91m ')
		mailll = open('cookiefb.txt','r').read()
		somailll = mailll.split('\n')
		cac = 0
		os.system("clear")
		print('\033[93m--------------------------\033[92m©\033[93m-----------------------------')
		print('\033[1m\033[97m[\033[1m\033[92m ∆ \033[97m] \033[96mCopyright by Mr cac\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mMOMO \033[90m:\033[96m0799078754\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mPAYPAL \033[90m:\033[96mofficialbalon2019@gmail.com\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mTELEGRAM \033[90m:\033[96mt.me/mr_caca\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mFACEBOOK \033[90m:\033[96mfb.com/danhcac.comm\033[92m ☑')
		print('\033[93m══════════════════════════════════════════════════════════')
		while True:
			for cookief1b in somailll:
				r33 = re.findall(r'c_user=.*?;', cookief1b)
				concacc = ''.join(r33)
				concacc = concacc.replace(";", "") 
				idcookie=concacc.split("=")[1]
				cookiefb={'cookie':cookief1b}
				respondse = requests.get("https://mbasic.facebook.com/", headers = cookiefb)
				if respondse.text.find("Đăng xuất") == -1:
					print('\033[97m'+idcookie +'\033[92m | '+'\033[91mCookie Die - Bỏ Qua')
				else:
					laytencookie= requests.get('https://mbasic.facebook.com',headers= cookiefb )
					xuatra = re.findall(r'Đăng xuất .*?<', laytencookie.text)
					tenfbne = ''.join(xuatra)
					tenfbne = tenfbne.replace("Đăng xuất", "") 
					tenfbne = tenfbne.replace("<", "")
					tenfbne1 = tenfbne.replace("(", "") 
					tencookie = tenfbne1.replace(")", "") 
					print('          \033[97m'+idcookie +'\033[96m|'+ '\033[97m'+tencookie+ '\033[96m|'+'\033[92mTiến Hành Làm ')
					r2= requests.get('https://traodoisub.com/api/?fields=page&access_token='+token)
					stringx5= r2.text.replace('"','uid')
					stringx4 = re.findall(r': uid.*?uid', stringx5)
					for url1 in stringx4:
						uidfb= url1.split('uid')[1]
						cookiefb={'cookie':cookief1b}
						keyurl = "https://mbasic.facebook.com/" + uidfb
						try:
							keyurlok = keyurl.replace("www.facebook.com","mbasic.facebook.com")
							kq = requests.get(keyurlok, headers= cookiefb) 
							geturl = re.findall(r'content="https:\/\/www.facebook.com\/.* \/><link ',kq.text)
							get_url_page = re.findall(r'https.*"', ''.join(geturl))
							get_url_page_ok = ''.join(get_url_page)
							get_url_page_ok = ''.join(get_url_page).replace("\"","")
							getpage = requests.get(get_url_page_ok.replace("www","mbasic"), headers = cookiefb)
							rg = re.findall(r'\/a\/profile.php?.*?Thích', getpage.text)
							stringx1 = ''.join(rg)
							uidlikepage = stringx1.split('"')[0].replace("amp;", "")
							likepage = requests.get('https://mbasic.facebook.com'+uidlikepage, headers = cookiefb)
						except Exception as e:
							print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
							continue
						idfollow= {'id':uidfb}
						cac = int(cac) +1 
						nhanxupage = requests.post("https://www.traodoisub.com/scr/nhantienpage.php", data = idfollow, headers = cookietds)
						if nhanxupage.text.find("2") == -1:
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
							print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mPAGE'+'\033[91m ▶Thành công')
						else:
							repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
							r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
							stringx4 = ''.join(r2)
							stringx4 = re.findall(r'>.*?<\/', stringx4)
							stringx5 = ''.join(stringx4)
							stringx5= stringx5.replace("</" , "")
							xubaygio = stringx5.replace(">","")
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
							print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mPAGE'+'\033[91m ▶\033[92m+600\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
						time.sleep(int(delay))
	if chonjob=='3':
		delay = input('\033[93mNhập Delay Giữa Mỗi Job \033[90m:\033[91m ')
		mailll = open('cookiefb.txt','r').read()
		somailll = mailll.split('\n')
		cac = 0
		os.system("clear")
		print('\033[93m--------------------------\033[92m©\033[93m-----------------------------')
		print('\033[1m\033[97m[\033[1m\033[92m ∆ \033[97m] \033[96mCopyright by Mr cac\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mMOMO \033[90m:\033[96m0799078754\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mPAYPAL \033[90m:\033[96mofficialbalon2019@gmail.com\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mTELEGRAM \033[90m:\033[96mt.me/mr_caca\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mFACEBOOK \033[90m:\033[96mfb.com/danhcac.comm\033[92m ☑')
		print('\033[93m══════════════════════════════════════════════════════════')
		while True:
			for cookief1b in somailll:
				r33 = re.findall(r'c_user=.*?;', cookief1b)
				concacc = ''.join(r33)
				concacc = concacc.replace(";", "") 
				idcookie=concacc.split("=")[1]
				cookiefb={'cookie':cookief1b}
				respondse = requests.get("https://mbasic.facebook.com/", headers = cookiefb)
				if respondse.text.find("Đăng xuất") == -1:
					print('\033[97m'+idcookie +'\033[92m | '+'\033[91mCookie Die - Bỏ Qua')
				else:
					laytencookie= requests.get('https://mbasic.facebook.com',headers= cookiefb )
					xuatra = re.findall(r'Đăng xuất .*?<', laytencookie.text)
					tenfbne = ''.join(xuatra)
					tenfbne = tenfbne.replace("Đăng xuất", "") 
					tenfbne = tenfbne.replace("<", "")
					tenfbne1 = tenfbne.replace("(", "") 
					tencookie = tenfbne1.replace(")", "") 
					cauhinhacc= requests.post('https://traodoisub.com/scr/api_dat.php?user='+tk+'&idfb='+idcookie)
					print('     \033[97m'+idcookie +'\033[96m|'+ '\033[97m'+tencookie+ '\033[96m|'+'\033[92mTiến Hành Làm ')
					r2= requests.get('https://traodoisub.com/api/?fields=like&access_token='+token)
					stringx5= r2.text.replace('"','uid')
					stringx4 = re.findall(r': uid.*?uid', stringx5)
					for url1 in stringx4:
						uidfb= url1.split('uid')[1]
						cookiefb={'cookie':cookief1b}
						urlstory = "https://mbasic.facebook.com/" + uidfb
						try:
							kq = requests.get(urlstory, headers = cookiefb)
							regex = re.findall(r'<meta property.*?<link rel', kq.text)
							regex = ''.join(regex)
							regex2 = re.findall(r'https://www.facebook.com/.* \/>',regex)
							regex2 = ''.join(regex2)
							linkok = regex2.replace(" />", "")
							linkok = linkok.replace("amp;", "")
							linkok = linkok.replace('"', "")
							linkok = linkok.replace("www","mbasic")
							respondse2 = requests.get(linkok, headers = cookiefb)
							regex3 = re.findall(r'/a/like.php?.*Thích</span>', respondse2.text)
							cut = ''.join(regex3)
							urlikeok = cut.split('"')[0].replace("amp;", "")
							likedone= requests.get('https://mbasic.facebook.com'+urlikeok, headers = cookiefb)
						except Exception as e:
							print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
							continue
						cac = int(cac) +1 
						idfollow= {'id':uidfb}
						nhanxupage = requests.post("https://traodoisub.com/ex/like/nhantien.php", data = idfollow, headers = cookietds)
						if nhanxupage.text.find("2") == -1:
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
							print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mLIKE'+'\033[91m ▶Thành công')
						else:
							repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
							r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
							stringx4 = ''.join(r2)
							stringx4 = re.findall(r'>.*?<\/', stringx4)
							stringx5 = ''.join(stringx4)
							stringx5= stringx5.replace("</" , "")
							xubaygio = stringx5.replace(">","")
							t1 = time.localtime()
							t = time.strftime("%H:%M:%S", t1)
							print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mLIKE'+'\033[91m ▶\033[92m+200\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
						time.sleep(int(delay))
	if chonjob=='4':
		delay = input('\033[93mNhập Delay Giữa Mỗi Job \033[90m:\033[91m ')
		mailll = open('cookiefb.txt','r').read()
		somailll = mailll.split('\n')
		cac = 0
		os.system("clear")
		print('\033[93m--------------------------\033[92m©\033[93m-----------------------------')
		print('\033[1m\033[97m[\033[1m\033[92m ∆ \033[97m] \033[96mCopyright by Mr cac\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mMOMO \033[90m:\033[96m0799078754\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mPAYPAL \033[90m:\033[96mofficialbalon2019@gmail.com\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mTELEGRAM \033[90m:\033[96mt.me/mr_caca\033[92m ☑')
		print('\033[97m[\033[92m ∆ \033[97m] \033[91mFACEBOOK \033[90m:\033[96mfb.com/danhcac.comm\033[92m ☑')
		print('\033[93m══════════════════════════════════════════════════════════')
		while True:
			for cookief1b in somailll:
				r33 = re.findall(r'c_user=.*?;', cookief1b)
				concacc = ''.join(r33)
				concacc = concacc.replace(";", "") 
				idcookie=concacc.split("=")[1]
				cookiefb={'cookie':cookief1b}
				respondse = requests.get("https://mbasic.facebook.com/", headers = cookiefb)
				if respondse.text.find("Đăng xuất") == -1:
					print('\033[97m'+idcookie +'\033[92m | '+'\033[91mCookie Die - Bỏ Qua')
				else:
					laytencookie= requests.get('https://mbasic.facebook.com',headers= cookiefb )
					xuatra = re.findall(r'Đăng xuất .*?<', laytencookie.text)
					tenfbne = ''.join(xuatra)
					tenfbne = tenfbne.replace("Đăng xuất", "") 
					tenfbne = tenfbne.replace("<", "")
					tenfbne1 = tenfbne.replace("(", "") 
					tencookie = tenfbne1.replace(")", "") 
					cauhinhacc= requests.post('https://traodoisub.com/scr/api_dat.php?user='+tk+'&idfb='+idcookie)
					print('        \033[97m'+idcookie +'\033[96m|'+ '\033[97m'+tencookie+ '\033[96m|'+'\033[92mTiến Hành Làm ')
					so= ['1','2','3']
					jobrandom = random.choice(so)
					if jobrandom=='1':
						r2= requests.get('https://traodoisub.com/api/?fields=follow&access_token='+token)
						stringx5= r2.text.replace('"','uid')
						stringx4 = re.findall(r': uid.*?uid', stringx5)
						for url1 in stringx4:
							
							uidfb= url1.split('uid')[1]
							cookiefb={'cookie':cookief1b}
							keyurl= ('https://www.facebook.com/profile.php?id='+uidfb)
							try:
								kq = requests.get(keyurl.replace("www", "mbasic"), headers= cookiefb)
								rg = re.findall(r'\/a\/subscribe?.*?refid=17', kq.text)
								stringx1 = ''.join(rg)
								stringx3 =  stringx1
								urlfollow = "https://mbasic.facebook.com/"+ stringx3
								urlfollow = urlfollow.replace("amp;", "")
								follow_ok = requests.get(urlfollow, headers = cookiefb)
							except Exception as e:
								print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
								continue
							idfollow= {'id':uidfb}
							cac = int(cac) +1 
							nhanxusub = requests.post("https://www.traodoisub.com/scr/nhantiensub.php", data = idfollow, headers = cookietds)
							if nhanxusub.text.find("2") == -1:
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mFOLLOW'+'\033[91m ▶Thành công')
							else:
								repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
								r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
								stringx4 = ''.join(r2)
								stringx4 = re.findall(r'>.*?<\/', stringx4)
								stringx5 = ''.join(stringx4)
								stringx5= stringx5.replace("</" , "")
								xubaygio = stringx5.replace(">","")
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mFOLLOW'+'\033[91m ▶\033[92m+600\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
							time.sleep(int(delay))
					if jobrandom=='2':
						r2= requests.get('https://traodoisub.com/api/?fields=page&access_token='+token)
						stringx5= r2.text.replace('"','uid')
						stringx4 = re.findall(r': uid.*?uid', stringx5)
						for url1 in stringx4:
							uidfb= url1.split('uid')[1]
							cookiefb={'cookie':cookief1b}
							keyurl = "https://mbasic.facebook.com/" + uidfb
							try:
								keyurlok = keyurl.replace("www.facebook.com","mbasic.facebook.com")
								kq = requests.get(keyurlok, headers= cookiefb) 
								geturl = re.findall(r'content="https:\/\/www.facebook.com\/.* \/><link ',kq.text)
								get_url_page = re.findall(r'https.*"', ''.join(geturl))
								get_url_page_ok = ''.join(get_url_page)
								get_url_page_ok = ''.join(get_url_page).replace("\"","")
								getpage = requests.get(get_url_page_ok.replace("www","mbasic"), headers = cookiefb)
								rg = re.findall(r'\/a\/profile.php?.*?Thích', getpage.text)
								stringx1 = ''.join(rg)
								uidlikepage = stringx1.split('"')[0].replace("amp;", "")
								likepage = requests.get('https://mbasic.facebook.com'+uidlikepage, headers = cookiefb)
							except Exception as e:
								print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
								continue
							idfollow= {'id':uidfb}
							cac = int(cac) +1 
							nhanxupage = requests.post("https://www.traodoisub.com/scr/nhantienpage.php", data = idfollow, headers = cookietds)
							if nhanxupage.text.find("2") == -1:
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mPAGE'+'\033[91m ▶Thành công')
							else:
								repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
								r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
								stringx4 = ''.join(r2)
								stringx4 = re.findall(r'>.*?<\/', stringx4)
								stringx5 = ''.join(stringx4)
								stringx5= stringx5.replace("</" , "")
								xubaygio = stringx5.replace(">","")
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mPAGE'+'\033[91m ▶\033[92m+600\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
							time.sleep(int(delay))
					if jobrandom=='2':
						r2= requests.get('https://traodoisub.com/api/?fields=like&access_token='+token)
						stringx5= r2.text.replace('"','uid')
						stringx4 = re.findall(r': uid.*?uid', stringx5)
						for url1 in stringx4:
							uidfb= url1.split('uid')[1]
							cookiefb={'cookie':cookief1b}
							urlstory = "https://mbasic.facebook.com/" + uidfb
							try:
								kq = requests.get(urlstory, headers = cookiefb)
								regex = re.findall(r'<meta property.*?<link rel', kq.text)
								regex = ''.join(regex)
								regex2 = re.findall(r'https://www.facebook.com/.* \/>',regex)
								regex2 = ''.join(regex2)
								linkok = regex2.replace(" />", "")
								linkok = linkok.replace("amp;", "")
								linkok = linkok.replace('"', "")
								linkok = linkok.replace("www","mbasic")
								respondse2 = requests.get(linkok, headers = cookiefb)
								regex3 = re.findall(r'/a/like.php?.*Thích</span>', respondse2.text)
								cut = ''.join(regex3)
								urlikeok = cut.split('"')[0].replace("amp;", "")
								likedone= requests.get('https://mbasic.facebook.com'+urlikeok, headers = cookiefb)
							except Exception as e:
								print('\033[91mCó Lỗi Khi Đang Làm Nhiệm Vụ',end='\r')
								continue
							idfollow= {'id':uidfb}
							cac = int(cac) +1 
							nhanxupage = requests.post("https://traodoisub.com/ex/like/nhantien.php", data = idfollow, headers = cookietds)
							if nhanxupage.text.find("2") == -1:
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str(cac)+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mLIKE'+'\033[91m ▶Thành công')
							else:
								repondse1 = requests.get("https://traodoisub.com", headers = cookietds)
								r2 = re.findall(r'soduchinh.*?xu', repondse1.text)
								stringx4 = ''.join(r2)
								stringx4 = re.findall(r'>.*?<\/', stringx4)
								stringx5 = ''.join(stringx4)
								stringx5= stringx5.replace("</" , "")
								xubaygio = stringx5.replace(">","")
								t1 = time.localtime()
								t = time.strftime("%H:%M:%S", t1)
								print('\033[92m[\033[93m'+str()+'\033[92m]\033[91m ▶'+ '\033[93m'+t+'\033[91m ▶'+'\033[92m'+uidfb+'\033[91m ▶\033[93mLIKE'+'\033[91m ▶\033[92m+200\033[91m▶\033[92mTổng\033[90m:\033[96m'+xubaygio)
							time.sleep(int(delay))
							
							
