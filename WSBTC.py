from telethon import TelegramClient,sync,events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors.rpcerrorlist import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from os import system
import sys,pyfiglet,json
from time import sleep
try:
            import requests
            from bs4 import BeautifulSoup
except:
            system("pip install request")
            system("pip install bs4")
            exit()

F = "\033[m"
C = "\033[01;36m"
AZ = "\033[01;34m"
A = "\033[01;33m"
VD = "\033[01;32m"
VM = "\033[01;31m"
R = "\033[01;35m"


    
def clear():
    system("clear")
    
    
def banner():
        clear()
        img = pyfiglet.figlet_format("WSBTC",font="cosmike")
        by = AZ+"By"+C+" @WestSideDev"+F+"\n"
        for ani in list(VD+img):
            print(ani,end="")
            sys.stdout.flush()
            sleep(0.005)
        for ani2 in list(by):
            print(ani2,end="")
            sys.stdout.flush()
            sleep(0.05)

def conexão():
        system("rm -rf session.session session.session-journal")
######## Você pega o ID e o HASH no site de API do Telegram ########
        api_id = 
        api_hash = 
        cliente = TelegramClient('session',api_id,api_hash)
        cliente.connect()
        if not cliente.is_user_authorized():
             try:
                 print()
                 telefone = input(R+"Digite seu número: "+F)
                 cliente.send_code_request(telefone)
                 eu = cliente.sign_in(telefone,code=input(R+"Digite o código: "+F))
                 perfil = cliente.get_me()
                 print(VD+"Bem Vindo",C+perfil.first_name)
             except SessionPasswordNeededError:
                      passw= input(R+"Digite sua senha: "+F)
                      eu = cliente.sign_in(phone=telefone,password=passw)
                      perfil = cliente.get_me()
                      print(VD+"Bem Vindo",C+perfil.first_name)
                  

def bot():
            api_id = 
            api_hash = 
            cliente = TelegramClient('session.session',api_id,api_hash)
            user_agent = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
            cliente.connect()
            chat_bot = cliente.get_entity("@BitcoinClick_bot")
            user_bot = "@BitcoinClick_bot"
            for auto in range(5):
                    sys.stdout.write(VM+"Visitando site\n"+F)
                    sys.stdout.flush()
                    cliente.send_message(entity=chat_bot,message="Visit sites")
                    sleep(3)
                    texto = cliente(GetHistoryRequest(peer=chat_bot,offset_date=None,offset_id=0,limit=1,add_offset=0,max_id=0,min_id=0,hash=0))
                  
                            

def menu1():
        banner()
        a = "\n"+A+"["+R+"1"+A+"]"+VM+"INICIAR SESSÃO"+"\n"+A+"["+R+"2"+A+"]"+VM+"VISIT SITES"+"\n"+A+"["+R+"3"+A+"]"+VM+"BALANCE"+F+"\n"
        for ani3 in list(a):
            print(ani3,end="")
            sys.stdout.flush()
            sleep(0.006)
        opc = int(input(A+"["+C+"0"+A+"]"+VM+">>>"+F))
        if opc == 1 :
            banner()
            conexão()
            bot()
            
        if opc == 2 :
            banner()
            bot()
        else:
           exit()
            
menu1()
