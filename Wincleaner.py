# sripted by samay 
# cybok hackers 
# 127.0.0.1:8080 port :
# Offensive Security Certified Professional ! 
# python3 database expert
# samay-vaim-virusman-acezinmaker - admins of script 
# members : virus! 

#-----------------------------Colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

#--------------Imports

import os 
import sys
from time import sleep
from colorama import Fore

#-------------------------programs 


logo = """\033[1;37m

\033[1;37m[!] \033[1;31mThis is use for JIDs generator, You can Unlimitedly Edit !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Samay-VIRUSMAN    -   
=  \033[1;31m .┌───  \033[1;37mB-Hat Samay            -   \033[34m[✔]     https://github.com/samay825        [✔]
\033[1;37m=    JID Generator - Pro          -   \033[34m[✔]            Version 2.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Samay               -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 2.0         -
\033[1;37m└-=============================   -

\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """
#---------------------------------------tiny programs 

def banner():
    print(logo)

def space():
    print('\n')
#-----------------------------------------move function 
def moveprogramfile(folder,files):
    for i in files:
        os.replace(i, f"{folder}/{i}")
# --------------------------------------creating folders
def samayfile(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# -------------------object oriented programming ! 

class Virus:
    project = 'Display!'
    def __init__(self):
        os.system('clear')
        banner()
        space()
    def Display(self):
        print(Fore.RED+"└─"+Fore.WHITE+"[ 1 ] Automatically Arrange Files : ")
        print(Fore.RED+"└─"+Fore.WHITE+"[ 2 ] Custom [available soon] : ")
        print(Fore.RED+"└─"+Fore.WHITE+"[ 3 ] Update : ")
        print(Fore.RED+"└─"+Fore.WHITE+"[ 4 ] Exit : ")
           
    @staticmethod
    def samay():
        space()
        try:
           samay_list = os.listdir()
           samay_list.remove('Wincleaner.py')
           display = int(input(r+"└─"+w+"\033[1;37mEnter Desire Option: "+r))  
           if display==1:
               samayfile("Images")
               samayfile("Vidoes")
               samayfile("Exe|Rars")
               samayfile("Documents")
               samayfile("Apk")
               samayfile("Music")

               samay_write_images = ['.png','.jpg','.jpeg','.gif','.3gp']
               samay_write_index = [i for i in samay_list if os.path.splitext(i)[1].lower() in samay_write_images]

               samay_write_videos = ['.mp4','.webm','.mkv','.flv','.avi']
               samay_write_video_index = [i for i in samay_list if os.path.splitext(i)[1].lower() in samay_write_videos]

               samay_write_exerar = ['.exe','.rar','.7z','.zip','.gar','.gz','.iso','.z','.ace','.tar']
               samay_write_exe_index = [i for i in samay_list if os.path.splitext(i)[1].lower() in samay_write_exerar]

               samay_write_documents = ['.txt','.doc','.ppt','.pptx','.xlsx','.pdf','.docx','.html','.py','.c','.php','.js']
               samay_write_documents_file = [i for i in samay_list if os.path.splitext(i)[1].lower() in samay_write_documents]

               samay_apk = ['.apk']
               samay_apk_index = [i for i in  samay_list if os.path.splitext(i)[1].lower() in samay_apk]
               
               samay_music = ['.mp3','.mp4eg','.wav','.m4a','msv','m4a']
               samay_music_index = [i for i in samay_list if os.path.splitext(i)[1].lower() in samay_music]

               moveprogramfile("Images", samay_write_images)
               moveprogramfile("Videos", samay_write_video_index)
               moveprogramfile("Exe|Rars", samay_write_exe_index)
               moveprogramfile("Documents", samay_write_documents_file)
               moveprogramfile("Apk", samay_apk_index)
               moveprogramfile("Music", samay_music_index)


               

                    

        except Exception as e:
            print("code error! ")   

         

        
if __name__ == '__main__':
   samay = Virus()
   samay.Display()
   samay.samay()