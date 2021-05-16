import subprocess
import os
import time
import sys


class bcolors:
    
    ERRO = '\033[91m'
    OK = '\033[94m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    AZUL = '\033[1;44m '
os.system("clear")
print(bcolors.WARNING + "AVISO: DESEJA CONTINUAR?sim[1]nao[2]" + bcolors.RESET)
escolha = int(input(""))
menu = 99
if escolha == 2:
    print("vai ver peppa")
    print("aborting...")
    time.sleep(2)
else:

    
    while menu  == 99 :
       
            os.system('clear')
        
          
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print("MMMNNmmmNmmNNNMMMMMMMMMNNmmmmmmNMNmmmmmmmmmmmmmmNNNMMMMMMMMMNMMMMMMMMMMMMMNNmmmmmmmmmmmmmNmNNNNMMNNMMNMMNNNNmmmmmmmNNNNNMMMMMNmmmmmmmmmmmNNNMMMMMMMMMMMMMNNmmmmmmmNNNMMMMMMNmNNmmmmmmmmmmmmmmmmmmmmNMMMM")
            print("MMMNmyyyyyyyyydNMMMMNdyyyyyyyyymMdyyyyyyyyyyyyyyyyyhdNMMMMMMMMMMMMMMMMMMMMNyyyyyyyyyyyyyyyyyyhmNMMNMMNNmhyyyyyyyyyyyyyydmMMNMdyyyyyyyyyyyyyyhmNMMMMMMNmhyyyyyyyyyyyyyhdNMMMNyyyyyyyyyyyyyyyyyyyyyyyhMMMM")
            print("NMMMdyyyyyhyyyyymMMmyyyyyhhyyyymMdhhhhhhhhhhhhhhyyyyyyhNNMMNMMMMNMNMMMMMMMNhhhhhhhhhhhhhhhyyyyyydNNNMmyyyyyyhhhhhhhyyyyyyhNNMdyhhhhhhhhhhyyyyyydMMMNmyyyyyyhhhhhhhyyyyyydNMNhhhhhhhhhhhhhhhhhhhhhhhdNNMM")
            print("MMMMdyyyymhmdyyyymmyyyydmhNhyyymMmhhhhhhhhhhhhhhhddhyyyymMMMMMMMNMMMMMMMMMMhhhhhhhhhhhhhhhdddyyyyhNMNyyyyhmdhhhhhhhdddyyyyhNMdhhhhhhhhhhhhddyyyyhNMmyyyydmdhhhhhhhdddyyyydMNhhhhhhhhhhhmdhhhhhhhhhhdMMMM")
            print("MMMMdyyyymyyNdyyyyyyyydNyymhyyymMdyyyyyyyyyyyyyyyyymdyyyhNMMNMMMNMNMNMMMMMMyyyyyyyyyyyyyyyyyymhyyydMdyyyymyyyyyyyyyyyhmyyyyNMdyyyyyyyyyyyyyhmyyyymMdyyyhmyyyyyyyyyyydmyyyhMNyyyyyyyyyyymhyyyyyyyyyydMMMM")
            print("NMMMdyyyymyyhNdyyyyyydNhyymhyyymMmdddddddddddddhyyyymyyyyNMMMMMMNMMMNMMMMMNddddddddddddddyyyyddyyyhMdyyyhdyyyymmmdyyyyNyyyyNMdyyydddddddyyyyddyyydMhyyyddyyyhmmmhyyyyNyyyyNNmmmmmmmyyyymhyyyhmmmmmmNMMMM")
            print("NMMMdyyyymyyyhNdyyyyhNhyyymhyyymMdyyyyyyyyyyyyyyyyyddyyyhNNMMMMMNMMMNMMMMMNyyyyyyyyyyyyyyyyyymhyyydMdyyyhdyyyhNNNmyyyyNyyyyNMdyyyyyyyyyyyyyymhyyydMhyyyddyyydNNMmyyyyNyyyyNMMMMMMMMhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyhNhyyhNhyyyymhyyymMdyyyyhyhhhhhhhhhddhyyyymNNMMMMMNNMMNMMMMMNyyyyyhhhhhhhhhhhddhyyyyNMdyyyhdyyyhMMNNyyyyNyyyyNNdyhhhhhhhhhhhdmhyyyhNNhyyyddyyyhMNMmyyyyNyyyyNMMMMNMMMhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyyhNhhNhyyyyyNhyyymMdyyydmhhhhhhmdhhyyyyyhmMNNMMMMMNMMMNMMMNMNyyyyNdhhhhhdmhhhyyyyyhNMMdyyyhdyyyhMMNNyyyyNyyyyNNdhhhhhhhhhhhdddyyyyhNNhyyyddyyyhMNMmyyyyNyyyyNMMMMMMMNhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyyyhNNhyyyyyymhyyymMdyyyddyyyyyyhmyyyyydmNNMNNMMNMMMMMMNMMMNMMyyyyNyyyyyyyhdyyyyydNMMMMdyyyhmyyyhNMNNyyyyNyyyyNMdyyyyyyyyyyyyyhmyyyymMhyyyddyyyhMMMmyyyyNyyyyNMMMMMMMMhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyyyyhhyyyyyyymhyyymMdyyyddyyyhyyyymyyyyNMMNMMMMMNMMMNMMNMMMNMNyyyyNyyyyhyyyhdyyyhNMMMMMdyyyhmyyyyNNmdyyyyNyyyyNNdyyhdddddddyyyyddyyyhMhyyyddyyyhmNNdyyyyNyyyyNMMMMMMMNhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyhyyyyyydyyyymhyyydMdyyyddyyyhmyyyymyyyyNMNMMMNNNMMNNMMNMMMNMNyyyyNhyyymdyyyhdyyyhNNMMMdyyyhmyyyyyyyyyyyhNyyyyNNdyyyyyyyyyyyyyymyyyydMdyyyhmyyyyyyyyyyyhmyyyyNMMMMMMMNhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyNdyyyyhNyyyymhyyydMdyyyddyyyhMmyyyymyyyymNMMMNNNNMMNMMMNMMNMMyyyymhyyymMdyyyhmyyyhNNMMNyyyydmhhyyhhyhhdmhyyyhNNdyhyyyyyyyyhhddhyyyhNMmyyyyddhhhyyyyhhdmyyyydNMMMMMMMNhyyymhyyydMMMMMMMMMMM")
            print("MMMMdyyyymyyyyNMhyyhNNyyyymhyyymMdyyyddyyyhMMmyyyymyyyymMMdyyyyNMNMMMMMMNMMyyyymhyyydMNdyyyhmyyyhNMMMmyyyyyhhhhhhhhhyyyyyhNNNdhhhhhhhhhhhhyyyyydNNMNdyyyyyyhhhhhhhhyyyyyhNNMMMMMMMNhyyymhyyydMMMMMMMMMMM")
            print("MMNMdyyyymyyyyNNNhyNMNyyyymhyyydNdyyyddyyyhMMMNyyyymhyyymMdyyyyNNNMMNMNMNNNyyyymhyyydMNNdyyyhdyyyhNMMMNdhyyyyyyyyyyyyyyhmNMMMdyyyyyyyyyyyyyyhdNNNMMMNNdyyyyyyyyyyyyyyyhmMMNMMMMMMMNyyyymhyyydMMMMMMMMMNM")
            print("MMMMNmmmmNmmmmNMMNNMMNmmmmNmmmmNMNmmmNNdmmmMMNMNmmmmNmmmmNmmmmmNMNMMNMNMNMNmmmmNmmmdNMNMNmmmdNmmmmNMNMMMMNmmmmmmmmmmmNNMNMMMNmmmmmdmmmdmmmmNNMNNNNMMNNMMNNmmmmmmmmmmNNNMMMNMMMMMMMNmdmmNmmmmmMMMMMMMMMMM")
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print(bcolors.ERRO + "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMNMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMNMMMMMNMMMNMMMNNMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"+bcolors.RESET)
            print(bcolors.WARNING+"\n\nPROGRAMA INICIANDO..."+bcolors.RESET) 

            print(bcolors.WARNING+"\n\n o que voce deseja fazer?"+bcolors.RESET)
            print("abrir ferramentas[1] abrir programas comuns[2] Instalar ferramentas[3]")
            escolha1 = int(input(""))
               
               
            #FERRAMENTAS
           
            
            if escolha1 ==1:
            
                       print(bcolors.OK+"Abrir metasploit[1] abrir nmap[2] abrir aircrackng[3] "+bcolors.RESET)
                       print(bcolors.ERRO+"Retornar ao menu[99]"+bcolors.RESET)
                       escolha2 = int(input(""))
                       if escolha2 == 99:
                               menu == 99
       
                       if escolha2 == 1:
                           print(bcolors.ERRO+"ATENCAO NAO NOS RESPONSABILISAMOS POR SEUS ATOS"+bcolors.RESET)
                           print(bcolors.WARNING+"O PROGRAMA A SEGUIR CONTEM ARQUIVOS PERIGOSOS ESTEJA CIENTE DISSO"+bcolors.RESET)
                           print(bcolors.OK+"ABRINDO MSFCONSOLE"+bcolors.RESET)
                           os.system('msfconsole')
       
                       if escolha2 == 2:
                           print(bcolors.OK+"ABRINDO NMAP"+bcolors.RESET)
                           os.system('nmap')
       
       
                      
       
                       if escolha2 == 3:
                           print(bcolors.OK+"ABRINDO AIRCRACK-NG"+bcolors.RESET)
                           os.system('aircrack-ng')
                       if escolha2 == 4:
                           os.system('Firefox')
            
            if escolha1 ==2:
                os.system("clear")
                   
                print("em construcao")
                
                time.sleep(3)
                
                menu == 99
                       
            

               #baixar ferramentas
            if escolha1 ==3:
                os.system("clear")
                print("Qual programa voce deseja instalar em sua maquina?(as ferramentas serao salvas na pasta tools")
                print(bcolors.OK+"nmap[1] metasploit[2] aircrack-ng[3]"+bcolors.RESET)
                print(bcolors.ERRO+"Retornar ao menu[99]"+bcolors.RESET)
                escolha3 = int(input(""))
                if escolha3 == 99:                        
                        menu == 99
                if escolha3 ==1:
                    processo = subprocess.call(["git clone https://github.com/nmap/nmap","mkdir tools"], shell=True)
                if escolha3 ==2:
                    processo = subprocess.call(["git clone https://github.com/rapid7/metasploit-framework.git","mkdir tools"], shell=True)
                if escolha3 ==3:
                    processo = subprocess.call(["git clone https://github.com/aircrack-ng/aircrack-ng.git","mkdir tools"], shell=True)



            
                
                
                        
            
                   
            



