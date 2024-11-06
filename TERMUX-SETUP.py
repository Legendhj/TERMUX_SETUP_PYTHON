import os,time
os.system('clear')
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
logo=f"""
{G}<----welcome to o termux-setup tool---->
▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄ 
▐▌     █   ▝▚▞▘ ▐▌   ▐▌  █
▐▛▀▀▘  █    ▐▌  ▐▛▀▀▘▐▌  █
▐▌   ▗▄█▄▖▗▞▘▝▚▖▐▙▄▄▖▐▙▄▄▀ 
==============================="""

def main():
	print(logo)
	print(f'{G}[1] SETUP FOR PYTHON SCRIPT RUN')
	print(f'{G}[2] SETUP FULL')
	print(f'[0] EXIT')
	print(30*f'=')
	option = input(f'[+] CHOICE : ')
	if option =='1':
		setup()
	else:
		print(f'[!] option not available')
		main()


def setup():
	print(f'{G}UPDATING YOUR TERMUX....')
	time.sleep(2)
	os.system('pkg update -y')
	print(f'{G}UPDATE Done'),time.sleep(1)
	os.system('clear')
	print(f'{G} INSTALLING.. git')
	time.sleep(2)
	os.system('pkg install git -y')
	print(f'{G}INSTALL DONE ✅'),time.sleep(1)
	os.system('clear')
	print(f'{G} INSTALLING... PYTHON2,3')
	os.system('pkg install python2')
	print(f'{G} INSTALL DONE'),time.sleep(1)
	print(f'{G} INSTALLING RESOURCES FOR PIP✅')
	os.system('pip install requests')
	os.system('pip install rich')
	os.system('pip install httpx')
	os.system('pip install random')
	os.system('pip install bs4')
	os.system('pip install re')
	os.system('pip install sys')
	os.system('pip install uuid')
	os.system('pip install datetime')
	os.system('pip install urllib')
	os.system('pkg install espeak -y')
	print(f'{G} CONGRATULATIONS 🎉 YOUR TERMUX SUCCESSFUL SETUP')
	os.system('espeak -a 300 "CONGRATULATIONS BOSS, YOUR TURMUX, SETUP COMPLETE"')
	os.system('rm -rf .bashrc')
	os.system('nano .bashrc')
	os.system('espeak -a 300 " please, past, the, code, provide, my, owner, of, you, and, press, control,+,x,+y,enter"')
	
	
	
	
	















main()