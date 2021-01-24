import itertools
import os,sys
import random
from time import sleep

# Banner
sleep(2)
print(" ")
print(""" \033[1;32;40m  ___________
 < wordl-genn! >              
   ———————————
                            (*) Basic Wordlist
      \                     (*) User
   \033[1;31;40m    \   ,__,             (*) Passwords
        \  (oo)____         (*) Generator
           (__)    )  \
                                                  ||--|| *                                          Wordlist Generator     [*] By : T3rr8us P74NK                                     [*] Team : CafSecHax                                       \033[1;32;40m[*] Website : https://anonymous                             -pyr4mid.blogspot.com/?m=1                                                """)
sleep(2)
print(""" 
\033[1;31;40m —————————————————————————————————————————————————————————
 \033[1;32;40m[+]> \033[1;31;40mInsert the information about the victim to make a      dictionary.
 
 \033[1;32;40m[+]>\033[1;31;40m Please Don't Skep :)!
 —————————————————————————————————————————————————————————""")
 
sleep(2)
print(" ")
print(" [x]> Insert Victim Info :")


# User Inputs
sleep(1)
print(" ")
input1 = input(" > Nickname : ")
sleep(1)
input2 = input(" > First Name : ")
sleep(1)
input3 = input(" > Last Name : ")
sleep(1)
print(" ")
print(" [-] You must enter 8 digits for birthday!")
input4 = input(" > Birth Date (DDMMYYYY) : ")
sleep(1)
print(" ")
input5 = input(" > Partners) Name : ")
sleep(1)
print(" [-] You must enter 8 digits for birthday!")
input6 = input(" > Partners) birthdate (DDMMYYYY) : ")
sleep(1)
print(" ")
input7 = input(" > Father Name : ")
sleep(1)
input8 = input(" > Mother Name : ")
sleep(1)
print(" ")
print(" [-] Put Info Keyword_1")
input9 = input(" > Keyword 1 : ")
sleep(1)
print(" [-] Put Info Keyword_2")
input10 = input(" > Keyword 2 : ")
sleep(1)
print(" [-] Put Info Keyword_3")
input11 = input(" > Keyword 3 : ")
sleep(1)
print(" [-] Put Info Keyword_4")
input12 = input(" > Keyword 4 : ")
sleep(1)
print(" [-] Put Info Keyword_5")
input13 = input(" > Keyword 5 : ")


# WordList Generator
list = list(map("".join, itertools.product(input1  , input2 , input3 , input4 , input5 , input6 , input7 , input8 , repeat=1)))


# Descriptions
sleep(1)
os.system("clear")
print("[+]> \033[1;32;40mDo You Want To Continue?")
print(" ")
print(" [1] Yes")
print(" [2] Exit")
print(" ")

choice = input("\033[1;31;40mSelect : ")

if choice == "1":
	os.system("clear")
	sleep(2)
	print(" ")
	print("\033[1;31;40m[ \033[1;32;40mGenerating \033[1;31;40m]##################################### ")
	sleep(2)
	print("\033[1;32;40m[+] Dont Copy The \033[1;31;40m>\033[1;37;40m , ' ] \033[1;31;40m<\033[1;37;40m")
	sleep(2)
	print(list)

if choice == "2":
	exit()

else:
	print(" \033[1;31;40m[~] Error Selected")		